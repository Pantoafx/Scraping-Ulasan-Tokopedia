Deskripsi: Repository ini berisi script Python yang mengotomatisasi proses pengambilan data ulasan pengguna dari Tokopedia menggunakan Selenium dan ChromeDriver. Script ini dirancang untuk mengumpulkan berbagai informasi ulasan seperti nama produk, konten ulasan, rating, dan tanggal. Data yang diambil akan disimpan dalam format CSV untuk analisis lebih lanjut, khususnya untuk analisis sentimen menggunakan algoritma pembelajaran mesin seperti Support Vector Machine (SVM).

Fitur:

    Mengambil data ulasan pengguna dari Tokopedia, termasuk nama produk, varian, isi ulasan, rating, dan tanggal ulasan.
    Interaksi otomatis dengan browser menggunakan Selenium dan ChromeDriver.
    Menyimpan data yang diambil ke dalam format CSV untuk kemudahan pengolahan data.
    Cocok untuk analisis sentimen dan analisis data e-commerce lainnya.

Persyaratan:

    Python 3.x
    Selenium
    ChromeDriver
    Pandas

Cara Penggunaan:

    Install semua dependensi yang dibutuhkan:
    pip install selenium pandas
    Unduh dan atur ChromeDriver sesuai dengan versi browser yang digunakan.
    Sesuaikan URL produk dalam script, lalu jalankan script untuk mulai scraping.
