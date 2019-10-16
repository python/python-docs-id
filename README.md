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
Anda bisa berkontribusi dengan:

* Membuat _pull requests_ di [repositori Github ini](https://github.com/python/python-docs-id/)
* Menerjemahkan langsung di [situs Transifex](https://www.transifex.com/python-doc/python-newest/language/id/)

### Beri Masukan
---
Merasa penerjemahannya tidak sesuai atau kurang cocok? Ayo diskusikan, buat [laporan isu di Github ini](https://github.com/python/python-docs-id/issues)
Masukan Anda sangat berarti untuk pengembangan penerjemahan dokumentasi Bahasa Pemrograman Python.

### Target (Fokus) Utama Penerjemahan
---
Sesuai informasi di PEP 545, bahwa terjemahan dokumentasi akan dimunculkan di pilihan bahasa (_Languange Switcher_),
setelah mencapai target berikut:

* 100% dari **bugs.po** dengan referensi yang memadai ke pelacak isu penyimpanan bahasa terjemahan :heavy_check_mark:
* 100% dari **tutorial**
* 100% dari **library/functions** (builtins) :heavy_check_mark:

##### Kami rekomendasikan agar Anda tidak mulai penerjemahan dari bagian "c-api" karena bagian itu berisi sangat teknis

##### Progres
* **tutorial/{appendix, appetite, datastructure, errors, index, inputoutput, interactive, interpreter, introduction, modules, stdlib, strlib2, venv, whatnow}** sudah diterjemahkan 100%
* **tutorial/{classes, controlflow, floatingpoint}** belum diterjemahkan

### Panduan Singkat Penerjemahan
---
Semua kata yang diapit dua tanda titik dua (:) **tidak perlu diterjemahkan**, termasuk juga kata yang diapit dua *backtick* (`) setelahnya, dan pastikan tidak ada spasi setelah titik dua yang kedua dengan *backtick* yang pertama. Berikut beberapa contohnya (kata yang ada dalam *backtick* dapat bervariasi).
```
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

### Daftar Istilah
---
Untuk memastikan konsistensi dari para penerjemah, berikut adalah sejumlah 
saran dan pengingat istilah yang sering digunakan.

Jangan ragu untuk memberi masukan.

Istilah | Terjemahan
--- | ---
*appetite* | selera
*arbitrary. arbitrarily.* | semena-mena, bergantian, berubah-ubah, acak. secara semena-mena.
*assigned. assignment* | diisi. mengisi, memberikan tugas, memberikan nilai 
*boolean* | *boolean*
*brace* | kurung kurawal
*buffer* | penyangga
*bug* | *bug*
*built-in* | bawaan
*cache* | *cache*
*changelog* | catatan perubahan
*compiler* | *compiler*
*concatenation. concatenated.* | perangkaian, penggabungan. digabungkan.
*custom* | ubahsuai, ubahsuaian
*debug* | *debug*
*decoding* | penerjemahan, *decoding*
*default* | bawaan
*deprecated* | usang
*dictionary* | *dictionary*
*docstring* | *docstring*
*download* | unduh
*e.g.* | mis.
*emitting* | mengirimkan
*encoding* | penyandian, *encoding*
*escape* | memisahkan
*etc.* | dll.
*exception* | pengecualian
*fall back* | beralih
*familiar* | terbiasa
*file* | berkas
*form* | bentuk, formulir
*framework* | kerangka, kerangka kerja
*header* | tajuk
*handling. handler.* | penanganan. penangan.
*hierarchy* | hierarki
*indentation* | indentasi
*interpreter* | *interpreter*
*invocation* | seruan, pemanggilan
*iterator* | *iterator*
*iterables* | *iterables*
*keyword* | kata kunci
*layout* | tata letak
*library* | pustaka
*loop* | perulangan, pengulangan
*namespace* | *namespace*
*null* | *null*
*ordering* | pengurutan, penyusunan
*override* | menimpa
*parse. parser. parsing* | urai. pengurai. mengurai.
*pass. passing. passed.* | langkah. melewatkan. diteruskan, dilewatkan.
*path* | jalur
*pickle* | *pickle*, acar, asinan, yang diawetkan
*placeholder* | *placeholder*, penampung
*prompt* | *prompt*
*raise* | menimbulkan, memunculkan
*range* | kisaran, rentang
*round* | pembulatan
*run* | operasikan
*runtime* | *runtime*
*signature* | *signature*, pengenal, tanda tangan
*site-packages* | *site-packages*
*slice* | iris, irisan
*snippet* | cuplikan
*stack trace* | tumpukan jejak
*startup* | permulaan
*stream* | aliran, *stream*
*template* | *template*, templat
*thread* | *thread*, utas
*trade-off* | mengorbankan
*tuple* | *tuple*
*upload* | unggah

### Keterangan Tambahan
---
Menempatkan aktivitas penerjemahan di tempat penyimpanan umum ini bertujuan untuk 
menarik dan mendapatkan lebih banyak kontribusi dibandingkan situs penerjemahan 
yang fungsinya sangat spesifik, seperti halnya Transifex.

Per tanggal **2019-10-15** repositori `python-docs-id` tersedia di bawah repositori Github organisasi Python.

https://github.com/python/python-docs-id/

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

### Referensi
---

* [PEP 545 -- Python Documentation Translations](https://www.python.org/dev/peps/pep-0545/)
* [Doc-SIG -- Python Documentation Special Interest Group](https://mail.python.org/mailman/listinfo/doc-sig)

