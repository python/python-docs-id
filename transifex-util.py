#!/usr/bin/env python
#
# This python file contains utility functions to manage a Python docs translation
# with Transifex.
#
# This file is maintained at: https://github.com/python-docs-translations/transifex-automations/blob/main/sample-workflows/transifex-util.py

import configparser
from argparse import ArgumentParser
import os
from contextlib import chdir
from pathlib import Path
from subprocess import call
import sys
from tempfile import TemporaryDirectory


def fetch():
    """
    Fetch translations from Transifex, remove source lines.
    """
    if (code := call("tx --version", shell=True)) != 0:
        sys.stderr.write("The Transifex client app is required.\n")
        exit(code)
    lang = LANGUAGE
    if PULL_OPTIONS:
        _call(f"tx pull -l {lang} --force {PULL_OPTIONS}")  # XXX Do we pull everything?
    else:
        _call(f"tx pull -l {lang} --force")
    for file in Path().rglob("*.po"):
        _call(f"msgcat --no-location -o {file} {file}")


def _call(command: str):
    if (return_code := call(command, shell=True)) != 0:
        exit(return_code)


def recreate_tx_config():
    """
    Regenerate Transifex client config for all resources.
    """
    with TemporaryDirectory() as directory:
        with chdir(directory):
            _clone_cpython_repo(VERSION)
            _build_gettext()
            with chdir(Path(directory) / "cpython/Doc/build"):
                _create_txconfig()
                _update_txconfig_resources()
                with open(".tx/config", "r") as file:
                    contents = file.read()
        contents = contents.replace("./<lang>/LC_MESSAGES/", "")

        os.makedirs(".tx", exist_ok=True)
        with open(".tx/config", "w") as file:
            file.write(contents)


def delete_obsolete_files():
    files_to_delete = list(_get_files_to_delete())
    if not files_to_delete:
        return
    else:
        for file in files_to_delete:
            print(f"Removing {file}")
            os.remove(file)
            _call(f'git rm --quiet "{file}"')


def _get_files_to_delete():
    with open(".tx/config") as config_file:
        config = config_file.read()
    for file in Path().rglob("*.po"):
        if os.fsdecode(file) not in config:
            yield os.fsdecode(file)


def _clone_cpython_repo(version: str):
    _call(
        f"git clone -b {version} --single-branch https://github.com/python/cpython.git --depth 1"
    )


def _build_gettext():
    _call("make -C cpython/Doc/ gettext")


def _create_txconfig():
    _call("sphinx-intl create-txconfig")


def _update_txconfig_resources():
    _call(
        f"sphinx-intl update-txconfig-resources --transifex-organization-name python-doc "
        f"--transifex-project-name {PROJECT_SLUG} --locale-dir . --pot-dir gettext"
    )


def _get_tx_token() -> str:
    if os.path.exists(".tx/api-key"):
        with open(".tx/api-key") as f:
            return f.read()

    config = configparser.ConfigParser()
    config.read(os.path.expanduser("~/.transifexrc"))
    try:
        return config["https://www.transifex.com"]["token"]
    except KeyError:
        pass

    return os.getenv("TX_TOKEN", "")


if __name__ == "__main__":
    RUNNABLE_SCRIPTS = ("fetch", "recreate_tx_config", "delete_obsolete_files")

    parser = ArgumentParser()
    parser.add_argument("cmd", choices=RUNNABLE_SCRIPTS)
    parser.add_argument("--language", required=True)
    parser.add_argument("--project-slug", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--pull-options", required=False)

    options = parser.parse_args()

    LANGUAGE = options.language
    PROJECT_SLUG = options.project_slug
    VERSION = options.version
    PULL_OPTIONS = options.pull_options

    globals()[options.cmd]()
