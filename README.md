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
* 100% dari **tutorial** :heavy_check_mark:
* 100% dari **library/functions** (builtins) :heavy_check_mark:

Target selanjutnya adalah **library/stdtypes** seperti yang disebutkan di situs devguide.

##### Kami rekomendasikan agar Anda tidak mulai penerjemahan dari bagian "c-api" karena bagian itu berisi sangat teknis

### Panduan Singkat Penerjemahan
---
Semua kata yang diapit dua tanda titik dua (:) **tidak perlu diterjemahkan**, termasuk juga kata yang diapit dua *backtick* (`) setelahnya, dan pastikan tidak ada spasi setelah titik dua yang kedua dengan *backtick* yang pertama. Berikut beberapa contohnya (kata yang ada dalam *backtick* dapat bervariasi).
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

### Daftar Istilah
---
Untuk memastikan konsistensi dari para penerjemah, berikut adalah sejumlah 
saran dan pengingat istilah yang sering digunakan.

Jangan ragu untuk memberi masukan.

Istilah | Terjemahan
--- | ---
*appetite* | selera
*approximation* | pendekatan, perkiraan
*arbitrary. arbitrarily.* | semena-mena, bergantian, berubah-ubah, acak. secara semena-mena.
*assigned. assignment* | diisi. mengisi, memberikan tugas, memberikan nilai 
*bind. binding. bound.* | mengikat. pengikatan. terikat.
*boolean* | *boolean*
*brace* | kurung kurawal
*breaking change* | perubahan yang merusak
*buffer* | penyangga
*bug* | *bug*
*built-in* | bawaan
*cache* | *cache*
*changelog* | catatan perubahan
*compiler* | *compiler*
*concatenation. concatenated.* | perangkaian, penggabungan. digabungkan.
*constructor* | *constructor*, pembangun
*container* | wadah, penampung
*custom* | ubahsuai, ubahsuaian
*debug* | *debug*
*decoding* | penerjemahan, *decoding*
*default* | bawaan
*deprecated* | usang
*dictionary* | *dictionary*
*docstring* | *docstring*, String Dokumentasi
*download* | unduh
*e.g.* | mis.
*emitting* | mengirimkan
*enclosing* | lampiran
*encoding* | penyandian, *encoding*
*escape* | memisahkan
*etc.* | dll.
*exception* | pengecualian
*fall back* | beralih
*familiar* | terbiasa
*fancy* | ajaib
*file* | berkas
*form* | bentuk, formulir
*floating point* | pecahan
*fraction* | pecahan
*framework* | kerangka, kerangka kerja
*generator* | pembangkit
*header* | tajuk
*handling. handler.* | penanganan. penangan.
*hierarchy* | hierarki
*indentation* | indentasi
*inheritance* | pewarisan
*instead* | alih-alih, dibandingkan (dengan)
*interpreter* | *interpreter*
*invocation* | seruan, pemanggilan
*iterator* | *iterator*
*iterables* | *iterables*
*keyword* | kata kunci
*layout* | tata letak
*library* | pustaka
*listcomp* | *listcomp*, *List Comprehension*, daftar pemahaman
*loop* | perulangan, pengulangan
*lossless* | berkurang
*maintain* | merawat, mempertahankan
*mangling* | *mangling*
*n/a* | t/a
*namespace* | *namespace*, ruang-nama
*null* | *null*
*ordering* | pengurutan, penyusunan
*override* | menimpa
*parse. parser. parsing* | urai. pengurai. mengurai.
*pass. passing. passed.* | langkah. melewatkan. diteruskan, dikirimkan.
*path* | jalur
*pickle* | *pickle*, acar, asinan, yang diawetkan
*placeholder* | *placeholder*, penampung
*private* | privat
*prompt* | *prompt*
*quirk* | kekhasan
*raise* | menimbulkan, memunculkan
*range* | kisaran, rentang
*rather* | alih-alih, dan bukan (dengan)
*reliable* | andal
*round* | pembulatan
*run* | operasikan
*runtime* | *runtime*
*scope* | lingkup, cakupan
*signature* | *signature*, pengenal, tanda tangan
*site-packages* | *site-packages*
*slice* | iris, irisan
*snippet* | cuplikan
*stack trace* | tumpukan jejak
*startup* | permulaan
*state* | kondisi, status
*stream* | aliran, *stream*
*suppressed* | dihilangkan, ditekan
*template* | *template*, templat
*thread* | *thread*, utas
*trade-off* | mengorbankan
*tuple* | *tuple*
*twist* | *twist*
*upload* | unggah

### Keterangan Tambahan
---
Menempatkan aktivitas penerjemahan di tempat penyimpanan umum ini bertujuan untuk 
menarik dan mendapatkan lebih banyak kontribusi dibandingkan situs penerjemahan 
yang fungsinya sangat spesifik, seperti halnya Transifex.

Per tanggal **2019-10-17** proses penerjemahan yang dibutuhkan sebagai minimum dari standar PEP 545 sudah selesai.

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

