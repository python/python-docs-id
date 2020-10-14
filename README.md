# Terjemahan Bahasa Indonesia untuk Dokumentasi Python
---

Perjanjian Kontribusi Dokumentasi

---

CATATAN TENTANG LISENSI UNTUK TERJEMAHAN: Dokumentasi Python dikelola 
menggunakan jaringan sukarelawan global. Dengan memasang proyek ini 
di Transifex, GitHub, dan tempat-tempat umum lainnya, dan mengundang
Anda untuk berpartisipasi, kami mengusulkan perjanjian dimana Anda akan
menyempurnakan dokumentasi Python atau terjemahan dokumentasi 
Python untuk digunakan oleh PSF di bawah lisensi CC0
(tersedia di
`https://creativecommons.org/publicdomain/zero/1.0/legalcode`_).
Sebagai imbal balik, Anda dapat secara terbuka mengambil reputasi untuk
bagian terjemahan dimana Anda berkontribusi dan jika terjemahan Anda 
diterima oleh PSF, Anda dapat (tetapi tidak diharuskan) mengirimkan 
tambahan termasuk penjelasan yang sesuai dalam berkas Misc/ACKS atau 
TRANSLATORS. Meskipun tidak ada dalam Perjanjian Kontribusi Dokumentasi
ini yang mewajibkan PSF untuk memasukkan kontribusi teks Anda, partisipasi 
Anda dalam Komunitas python disambut baik dan dihargai.

Anda dianggap menerima perjanjian ini, dengan mengirimkan pekerjaan
Anda ke PSF untuk dimasukkan dalam dokumentasi.

[sumber dokumen asli perjanjian dalam bahasa Inggris](https://www.python.org/dev/peps/pep-0545/#setup-the-documentation-contribution-agreement)

### Berkontribusi untuk Menerjemahkan
---
Situs dokumentasi Python Bahasa Indonesia: **https://docs.python.org/id/3.9/**

Repositori ini berisi [berkas-berkas ".po"](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html) dari [dokumentasi Python](https://docs.python.org/id/3.9/), yang akan dan sudah diterjemahkan dari Bahasa Inggris ke Bahasa Indonesia. Baca daftar pekerjaan yang **akan dan sedang dikerjakan** di [papan proyek](https://github.com/python/python-docs-id/projects/1).

Anda bisa berkontribusi dengan:

* Membuat _Pull Requests_ di [repositori Github ini](https://github.com/python/python-docs-id/), saat ini yang aktif adalah [branch 3.9](https://github.com/python/python-docs-id/tree/3.9)
* Menerjemahkan langsung di [situs Transifex](https://www.transifex.com/python-doc/python-newest/). Ikuti [Video (7 menit)](https://youtu.be/tg5kUJB2WLA) cara menggunakan Transifex.

Jika Anda tidak menggunakan Transifex, untuk mengubah berkas ".po" dibutuhkan aplikasi editor, misalnya: [POEdit](https://poedit.net/) tersedia multiplatform, [KDE Lokalize](https://kde.org/applications/development/org.kde.lokalize) hanya untuk Linux dengan KDE, atau banyak lagi [pilihan lainnya](https://en.wikipedia.org/wiki/Comparison_of_computer-assisted_translation_tools).

##### Kami rekomendasikan agar Anda tidak mengubah dengan teks editor pada umumnya, kecuali anda sudah mengerti [format file .po](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)

### Beri Masukan
---
Merasa penerjemahannya tidak sesuai atau kurang cocok? Ayo diskusikan, buat [laporan isu di Github ini](https://github.com/python/python-docs-id/issues)

Masukan Anda sangat berarti untuk pengembangan penerjemahan dokumentasi Bahasa Pemrograman Python.

### Target (Fokus) Utama Penerjemahan
---
Sesuai informasi di PEP 545, bahwa terjemahan dokumentasi akan dimunculkan di pilihan bahasa (_Languange Switcher_),
setelah mencapai target berikut:

* 100% dari **bugs.po** dengan referensi yang memadai ke pelacak isu penyimpanan bahasa terjemahan :heavy_check_mark:
* 100% dari **tutorial** :heavy_check_mark:
* 100% dari **library/functions** (builtins) :heavy_check_mark:

Target selanjutnya sudah dituliskan di [papan proyek](https://github.com/python/python-docs-id/projects/1#column-6851563). Anda bisa memulai dengan menerjemahkan kata atau kalimat yang pendek terlebih dahulu.

##### Kami rekomendasikan agar Anda tidak mulai penerjemahan dari bagian "c-api" karena bagian itu berisi sangat teknis

### Panduan Singkat Penerjemahan
---
Semua kata yang diapit dua tanda titik dua (:) **tidak perlu diterjemahkan**, hanya terjemahkan kata yang diapit dua *backtick* (`) setelahnya jika diperlukan, misalnya kata atau kalimat tersebut bukan sebuah nama, istilah atau konstanta.

Pastikan tidak ada spasi setelah titik dua yang kedua dengan *backtick* yang pertama. Berikut beberapa contohnya (kata yang ada dalam *backtick* dapat bervariasi, dan hanya diterjemahkan jika diperlukan).
```
:attr:`the_answer`
:class:`~decimal.Decimal`
:const:`True`
:data:`sys.stdout`
:dfn:`serializing`
:exc:`KeyboardInterrupt`
:envvar:`PATH`
:file:`.profile`
:func:`print`
:issue:`36817`
:keyword:`try`
:kbd:`Delete`
:meth:`~list.append`
:mod:`sitecustomize`
:newsgroup:`comp.lang.python`
:option:`-s`
:pep:`475`
:program:`chmod`
:samp:`{n}`
:source:`Lib/html/entitas.py`
:term:`>>>`
```

Semua kata yang diapit dua tanda *backtick* berganda (``), atau di Transifex disebut sebagai "Custom Variable",  **tidak perlu diterjemahkan**. Berikut beberapa contohnya.
```
``#!``
``'\n'``
``'\r\n'``
``'#'``
``.py``
``python.exe``
``.pyw``
```

Kata atau kalimat yang diapit dua tanda bintang (*), akan dituliskan sebagai penulisan miring (*italic*). Sehingga sesuaikan dengan konteksnya, apakah perlu diterjemahkan atau tetap dipertahankan sebagai kata atau kalimat dalam penulisan miring. Misalnya tidak perlu diterjemahkan jika atau kalimat itu merupakan nama, istilah atau konstanta.

### Daftar Istilah
---
Untuk memastikan konsistensi dari para penerjemah, [berikut](https://github.com/python/python-docs-id/wiki/Daftar-Istilah) adalah sejumlah saran dan pengingat istilah yang sering digunakan.

Jangan ragu untuk memberi masukan. Daftar istilah tersedia di [wiki](https://github.com/python/python-docs-id/wiki/Daftar-Istilah).

### Keterangan Tambahan
---
Menempatkan aktivitas penerjemahan di tempat penyimpanan umum ini bertujuan untuk menarik dan mendapatkan lebih banyak kontribusi dibandingkan situs penerjemahan yang fungsinya sangat spesifik, seperti halnya Transifex.

Per tanggal **2020-10-15** dokumentasi Python Bahasa Indonesia sudah tersedia di **https://docs.python.org/id/3.9/**

Per tanggal **2019-10-21** dokumentasi Python Bahasa Indonesia sudah tersedia di **https://docs.python.org/id/3.8/**

Per tanggal **2019-10-17** proses penerjemahan yang dibutuhkan sebagai minimum dari standar PEP 545 sudah selesai.

Per tanggal **2019-10-15** repositori `python-docs-id` tersedia di bawah repositori Github organisasi Python. **https://github.com/python/python-docs-id/**

### Perintah Transifex
---
Untuk mengambil data sumber dan terjemahan yang lebih baru (dibatasi hanya Bahasa Indonesia `id`) dari Transifex:
```
tx pull -l id
```

Untuk mengirim pembaruan ke Transifex:
```
tx push -t
```

Untuk mengirim pembaruan spesifik "resource" (misalnya python-newest.tutorial--interactive):
```
tx push -t -r python-newest.tutorial--interactive
```

Untuk sinkronisasi ulang berkas-berkas terbaru dari proyek **python-newest**:
```
tx config mapping-remote https://www.transifex.com/python-doc/python-newest/
```

### Membangun Berkas-berkas ".po" ini Menjadi Dokumentasi Python

Tujuan utama dari penerjemahan berkas ".po" adalah menerjemahkan situs [Dokumentasi Python](https://docs.python.org).

Untuk membangun (_build_) dari berkas-berkas ini agar menjadi dokumentasi lengkap, langkahnya baru dicoba di sistem operasi Linux dan Mac tersedia di [wiki](https://github.com/python/python-docs-id/wiki/Membangun-Dokumentasi-Python-di-Komputer).

### Referensi
---

* [PEP 545 -- Python Documentation Translations](https://www.python.org/dev/peps/pep-0545/)
* [Doc-SIG -- Python Documentation Special Interest Group](https://mail.python.org/mailman/listinfo/doc-sig)

