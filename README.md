# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan fiktif bernama **Jaya Jaya Maju** adalah sebuah perusahaan yang bergerak di bidang *edutech* dan tengah mengalami tantangan serius dalam departemen Human Resources (HR), yaitu **tingginya tingkat attrition (keluar dari perusahaan)**. Angka ini telah melebihi ambang batas wajar, yaitu 10%, dan dinilai dapat memberikan dampak negatif terhadap operasional dan keberlanjutan bisnis perusahaan.

Manajemen perusahaan ingin mengambil langkah preventif dan strategis untuk memahami penyebab utama dari tingginya attrition ini. Oleh karena itu, proyek ini bertujuan untuk menyelidiki data karyawan yang tersedia, mengeksplorasi pola-pola yang tersembunyi, serta memberikan visualisasi dashboard dan model prediksi yang dapat membantu pihak HR dalam mengambil keputusan yang lebih efektif.

### Permasalahan Bisnis

Berikut adalah permasalahan yang ingin diselesaikan melalui proyek ini:

1. **Tingginya tingkat attrition** yang berpotensi merugikan perusahaan jika tidak segera ditangani.
2. Kurangnya informasi dan pemahaman mengenai **faktor-faktor apa saja yang paling memengaruhi keputusan karyawan untuk keluar**.
3. Tidak adanya **alat pemantauan visual (dashboard)** yang dapat digunakan oleh HR untuk memantau kondisi dan metrik penting secara real-time.
4. Belum adanya sistem berbasis prediksi yang mampu mengidentifikasi karyawan yang berisiko tinggi untuk mengundurkan diri.


### Cakupan Proyek

Untuk menjawab permasalahan bisnis di atas, berikut adalah cakupan proyek yang akan dilakukan:

1. Melakukan analisis data menggunakan Python (Jupyter/Colab).
2. Melakukan eksplorasi dan visualisasi data untuk menemukan pola-pola signifikan dalam data HR.
3. Mengidentifikasi faktor-faktor utama yang memengaruhi attrition karyawan, seperti usia, departemen, gaji, tingkat kepuasan kerja, dan jarak rumah ke kantor.
4. Membuat **dashboard bisnis interaktif** menggunakan tools metabase untuk membantu HR memonitor attrition secara real-time.
5. Membangun model machine learning untuk memprediksi kemungkinan karyawan akan resign.
6. Mendokumentasikan seluruh proses dan insight dalam file Markdown (`README.md`) serta menyusun `requirements.txt` agar proyek dapat direplikasi dengan mudah.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

Proyek ini dikembangkan menggunakan Python dan disarankan untuk dijalankan dalam lingkungan virtual (virtual environment) untuk mengelola dependensi secara terisolasi.

Membuat dan Mengaktifkan Virtual Environment (venv) Buka terminal atau command prompt, lalu ikuti langkah-langkah berikut:

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_attrition python=3.9
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_attrition
    ```
4. Menginstal Dependensi dari requirements.txt Pastikan telah mengaktifkan virtual environment.
    ```
    pip install -r requirements.txt
    ```
5. Cara Menjalankan Skrip Python (.py) Setelah virtual environment diaktifkan dan semua dependensi terinstal, maka dapat menggunakan perintah berikut.
    ```
    python prediction.py
    ```
7. Hasil analisis, model yang ke file hasil_inference.csv.

## Business Dashboard

Email dan password Metabase

Email: root@mail.com

Password: root123

Dashboard ini dirancang untuk memberikan wawasan strategis mengenai fenomena attrition (pengunduran diri karyawan) di perusahaan. Melalui visualisasi data interaktif yang dibangun menggunakan Metabase dan terkoneksi ke database PostgreSQL melalui Docker, dashboard ini menyajikan analisis menyeluruh terhadap faktor-faktor utama yang memengaruhi keputusan karyawan untuk mengundurkan diri.

1. Attrition Rate Secara Keseluruhan
- Visualisasi: Kartu ringkasan (Summary Card) & Diagram Donut

- Insight:

    - Menampilkan rasio karyawan yang resign (Keluar) terhadap total populasi karyawan.

    - Dalam dashboard Anda, ditemukan bahwa sekitar 17% karyawan telah mengundurkan diri.

    - Memberikan indikator awal tingkat turnover perusahaan secara umum.

2. Faktor-Faktor Utama yang Mempengaruhi Keputusan Resign
- Visualisasi: Bar Chart Horizontal (Row Chart)

- Sumber Data: Hasil dari feature importance model prediktif

- Top 5 Faktor:

    - DistanceFromHome (0.78)

    - MonthlyRate (0.023)

    - NumCompaniesWorked (0.037)

    - PercentSalaryHike (0.0049)

    - PerformanceRating (0.0078)

- Insight: Faktor DistanceFromHome memiliki kontribusi paling besar terhadap kemungkinan resign. Faktor kompensasi dan riwayat kerja juga berperan penting.

3. Rata-Rata Gaji dan Jarak Tempuh
- Visualisasi: Summary Cards

- Insight:

    - Rata-rata Monthly Rate: ± $14,267.28

    - Rata-rata Distance From Home: 15 satuan (kemungkinan km atau miles)

    - Memberikan gambaran umum kondisi ekonomi dan geografi karyawan secara rata-rata.

4. Distribusi Status Attrition
- Visualisasi: Diagram Donut

- Insight:

    - Menampilkan proporsi antara karyawan yang Tetap dan Keluar.

    - Mayoritas karyawan masih bertahan (sekitar 83%).

5. Pengaruh Jarak Tempuh terhadap Tingkat Attrition
- Visualisasi: Bar Chart (8 Bins dari DistanceFromHome)

- Insight:

    - Terlihat tren bahwa semakin jauh jarak tempuh, semakin tinggi tingkat pengunduran diri.

    - Menunjukkan potensi kelelahan akibat komuter jarak jauh sebagai faktor retensi.

6. Pengaruh Gaji Bulanan terhadap Status Attrition
- Visualisasi: Bar Chart

- Insight:

    - Karyawan yang mengundurkan diri memiliki MonthlyRate yang secara agregat lebih rendah dibanding yang bertahan.

    - Memberikan sinyal bahwa kompensasi mungkin menjadi faktor motivasi untuk keluar.




## Conclusion

Proyek Employee Attrition Business Dashboard ini dirancang untuk menjawab permasalahan utama yang dihadapi oleh departemen HR, yaitu tingginya tingkat pengunduran diri (attrition) karyawan yang berdampak pada stabilitas dan produktivitas perusahaan.

Melalui analisis data historis karyawan dan visualisasi interaktif di Metabase, diperoleh insight strategis yang menjawab problem statement:

1. Tingkat Attrition Karyawan

- Sebanyak 17% dari total karyawan tercatat mengundurkan diri. Angka ini menunjukkan bahwa hampir 1 dari 6 karyawan memilih untuk keluar, yang menandakan adanya isu serius terkait retensi tenaga kerja.

2. Faktor-Faktor Utama Penyebab Attrition

- Berdasarkan hasil analisis model dan visualisasi, ditemukan 5 faktor utama yang paling berpengaruh terhadap attrition:

    - DistanceFromHome (jarak tempuh dari rumah ke kantor) menjadi faktor dominan.

    - Disusul oleh MonthlyRate (gaji bulanan), jumlah perusahaan sebelumnya (NumCompaniesWorked), kenaikan gaji (PercentSalaryHike), dan performance rating.

- Karyawan dengan jarak tempuh jauh lebih cenderung resign dibanding yang tinggal lebih dekat.

3. Karakteristik Karyawan yang Cenderung Keluar

- Visualisasi menunjukkan bahwa:

    - Karyawan yang keluar cenderung memiliki gaji lebih rendah.

    - Mereka juga memiliki jarak tempuh yang lebih jauh dari tempat tinggal ke kantor.

- Artinya, faktor ekonomi dan kenyamanan perjalanan berkontribusi besar terhadap keputusan untuk resign.

4. Rata-Rata Statistik Karyawan

- Rata-rata gaji bulanan berada di kisaran $14,267, sementara rata-rata jarak tempuh sekitar 15 km. Nilai-nilai ini menjadi referensi penting untuk merumuskan kebijakan retensi.


### Rekomendasi Action Items

Berdasarkan wawasan dari Employee Attrition Dashboard, berikut adalah langkah-langkah strategis yang dapat diterapkan oleh perusahaan untuk menurunkan tingkat pengunduran diri karyawan secara proaktif:

1. Optimalisasi Lokasi Kerja dan Fleksibilitas Komute

- Mengingat DistanceFromHome merupakan faktor paling signifikan terhadap attrition, perusahaan disarankan untuk:

    - Menyediakan opsi remote working atau hybrid system bagi karyawan dengan jarak tempuh jauh.

    - Menyusun kebijakan relokasi atau penempatan karyawan lebih dekat dari domisili.

2. Intervensi Dini terhadap Karyawan dengan Riwayat Perpindahan Pekerjaan

- Data menunjukkan bahwa karyawan dengan jumlah perusahaan sebelumnya (NumCompaniesWorked) yang tinggi lebih berisiko resign.

    - Implementasikan employee engagement program, seperti coaching atau mentorship, untuk kelompok ini.

    - Bangun jalur karier internal yang menarik untuk menumbuhkan loyalitas jangka panjang.

3. Perbaikan Struktur Kompensasi

- Karyawan dengan MonthlyRate rendah cenderung lebih sering resign.

    - Lakukan evaluasi menyeluruh terhadap skema kompensasi dan pastikan kompetitif terhadap pasar.

    - Tambahkan insentif kinerja atau tunjangan berbasis jarak dan kehadiran untuk mendorong retensi.

4. Perkuat Lingkungan Apresiatif dan Pengembangan Karyawan

- Meskipun PerformanceRating tidak terlalu signifikan dalam model, membangun budaya kerja yang menghargai kontribusi karyawan tetap penting.

    - Terapkan sistem penghargaan dan pengakuan rutin.

    - Berikan akses pada program pelatihan dan pengembangan diri yang relevan.

5. Monitoring dan Evaluasi Berbasis Data

- Jadikan metrik-metrik utama dalam dashboard (seperti attrition rate, jarak, gaji, dll.) sebagai early indicators untuk mendeteksi potensi pengunduran diri.

    - Lakukan evaluasi berkala berbasis dashboard ini untuk membantu tim HR membuat keputusan yang lebih cepat, akurat, dan preventif.

Dengan menerapkan strategi-strategi di atas, perusahaan tidak hanya dapat mengurangi tingkat attrition, namun juga membangun budaya kerja yang lebih sehat, loyal, dan berkelanjutan.
