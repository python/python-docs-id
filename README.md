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

### Berkontribusi untuk menerjemahkan
---
Anda bisa berkontribusi dengan:

* Membuat _pull requests_ di Github ini
* Menerjemahkan langsung di [situs Transifex](https://www.transifex.com/python-doc/python-newest/language/id/)

##### Kami rekomendasikan agar Anda tidak mulai penerjemahan dari bagian "c-api" karena bagian itu berisi sangat teknis

### Daftar Istilah
---
Untuk memastikan konsistensi dari para penerjemah, berikut adalah sejumlah 
saran dan pengingat istilah yang sering digunakan.

Jangan ragu untuk memberi masukan.

Istilah | Terjemahan
--- | ---
*bug* | bug
*download* | unduh
*interpreter* | interpreter
*upload* | unggah

### Keterangan Tambahan
---
Menempatkan aktivitas penerjemahan di tempat penyimpanan umum ini bertujuan untuk 
menarik dan mendapatkan lebih banyak kontribusi dibandingkan situs penerjemahan 
yang fungsinya sangat spesifik, seperti halnya Transifex.

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

