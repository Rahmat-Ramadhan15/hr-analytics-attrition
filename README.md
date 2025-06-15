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
5. Cara Menjalankan Skrip Python (.py) Setelah virtual environment diaktifkan dan semua dependensi terinstal, maka dapat dijalankan skrip utama proyek. Skrip utama adalah notebook.py. Hasil analisis, model yang ke filehasil_inference.csv.

## Business Dashboard

Dashboard ini dirancang untuk memberikan wawasan bisnis terkait attrition (pengunduran diri karyawan) di perusahaan, dengan menampilkan data visual yang mudah dipahami guna membantu pengambilan keputusan strategis oleh manajemen.

Dashboard dibangun menggunakan Metabase dan terhubung ke database PostgreSQL melalui Docker, menyajikan analisis berbasis data terkait faktor-faktor utama yang memengaruhi pengunduran diri karyawan.

1. Perbandingan Jumlah Karyawan yang Keluar dan Tidak (Attrition)
Visualisasi: Bar Chart

Menampilkan jumlah karyawan yang keluar (attrition = 1) dan tetap (attrition = 0).

Insight: Mengetahui seberapa besar tingkat pengunduran diri di perusahaan secara keseluruhan.

2. Top 5 Faktor yang Mempengaruhi Attrition
Visualisasi: Row Chart

Berdasarkan hasil feature importance (nilai korelasi atau kontribusi model), ditampilkan lima faktor teratas:

- DistanceFromHome (0.78) semakin jauh jarak rumah ke kantor, semakin besar kemungkinan karyawan mengalami kelelahan dan stres, sehingga berpotensi lebih tinggi untuk mengundurkan diri.

- NumCompaniesWorked (0.037) karyawan dengan riwayat bekerja di banyak perusahaan mungkin memiliki loyalitas rendah atau ekspektasi tinggi, yang memengaruhi kemungkinan keluar dari perusahaan.

- MonthlyRate (0.023) karyawan dengan gaji bulanan yang lebih rendah cenderung merasa kurang dihargai, yang dapat meningkatkan risiko keluar.

- PerformanceRating (0.0078) penilaian kinerja rendah dapat mencerminkan ketidakpuasan karyawan atau manajemen terhadap karyawan, yang berpotensi menyebabkan attrition.

- PercentSalaryHike (0.0049) karyawan dengan kenaikan gaji yang kecil bisa merasa tidak dihargai dan termotivasi untuk mencari peluang lain.

Insight: Mengetahui faktor mana yang paling dominan mempengaruhi keputusan resign.

3. Rata-rata Gaji Bulanan dan Jarak Rumah ke Kantor
Visualisasi: Kartu Ringkasan / Summary

Menampilkan:

- Rata-rata MonthlyRate

- Rata-rata DistanceFromHome

Insight: Memberikan gambaran umum kondisi rata-rata karyawan.

4. Hubungan Distance From Home dan Attrition
Visualisasi: Bar Chart

Menampilkan jumlah karyawan berdasarkan DistanceFromHome yang dikelompokkan berdasarkan status Attrition.

Insight: Apakah karyawan dengan jarak rumah yang lebih jauh cenderung lebih sering resign?

5. Hubungan MonthlyRate dan Attrition
Visualisasi: Bar Chart atau Line Chart (alternatif Boxplot jika tersedia)

- Menampilkan distribusi MonthlyRate untuk masing-masing status Attrition.

Insight: Apakah gaji bulanan berpengaruh terhadap keputusan resign?


## Conclusion

Proyek Employee Attrition Business Dashboard ini berhasil memberikan insight yang mendalam mengenai perilaku karyawan terkait pengunduran diri (attrition) berdasarkan data historis perusahaan.

Melalui visualisasi interaktif yang dibangun di Metabase, pengguna dapat:

1. Dengan mudah mengidentifikasi tingkat attrition secara keseluruhan.

2. Mengetahui lima faktor utama yang paling memengaruhi keputusan karyawan untuk resign, dengan DistanceFromHome sebagai faktor dominan.

3. Memahami hubungan antara variabel penting seperti MonthlyRate dan DistanceFromHome terhadap status attrition.

4. Mendapatkan gambaran umum kondisi karyawan melalui statistik rata-rata.

Dengan dashboard ini, manajemen dan tim HR dapat membuat keputusan strategis berbasis data untuk:

1. Meningkatkan retensi karyawan.

2. Merancang kebijakan kerja yang lebih adaptif dan human-centric.

3. Mengantisipasi potensi pengunduran diri secara lebih proaktif.

4. Dashboard ini menjadi landasan penting dalam membangun data-driven HR strategy untuk menciptakan lingkungan kerja yang lebih stabil dan produktif.

### Rekomendasi Action Items

Berdasarkan temuan dari dashboard, berikut beberapa rekomendasi yang dapat diterapkan perusahaan untuk menurunkan tingkat attrition:

1. Evaluasi dan fasilitasi transportasi atau fleksibilitas lokasi kerja, terutama bagi karyawan dengan DistanceFromHome yang jauh, mengingat jarak rumah ke kantor merupakan faktor paling signifikan terhadap attrition.

2. Lakukan program engagement untuk karyawan dengan riwayat berpindah kerja lebih dari sekali, karena data menunjukkan NumCompaniesWorked turut memengaruhi kemungkinan resign.

3. Tinjau kembali kebijakan kenaikan gaji dan kompensasi bulanan, terutama untuk kelompok karyawan dengan MonthlyRate dan PercentSalaryHike rendah, guna meningkatkan retensi.

4. Perkuat budaya apresiasi dan pengembangan karyawan, walau PerformanceRating memiliki pengaruh kecil, menjaga kepuasan dan motivasi tetap penting untuk mencegah turnover.

5. Lakukan monitoring berkala terhadap metrik-metrik utama dalam dashboard ini dan gunakan sebagai indikator awal dalam strategi retensi dan pengembangan SDM.

## Email dan password Metabase
Email: root@mail.com

Password: root123
