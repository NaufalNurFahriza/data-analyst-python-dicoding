# Project Analisis Data: Bike Sharing Dataset

Repository ini berisi proyek data analytics yang saya kerjakan. Proyek ini dideploy menggunakan **Streamlit**.

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-analyst-python-bike-sharing.streamlit.app/)

## Deskripsi
Proyek ini bertujuan untuk menganalisis data pada **Bike Sharing Dataset**. Tujuan akhirnya adalah untuk menghasilkan wawasan dan informasi yang berguna dari data yang dianalisis. Analisis ini mencakup:
1. **Penyewaan Sepeda per Jam**: Mengetahui jam dengan penyewaan sepeda terbanyak dan terdikit.
2. **Pengaruh Suhu terhadap Penyewaan Sepeda**: Menganalisis bagaimana suhu memengaruhi jumlah penyewaan sepeda.

## Struktur Direktori
```
Data-analyst-python-dicoding/
├── data/
│   ├── day.csv
│   └── hour.csv
├── dashboard/
│   └── dashboard.py
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt
```

### Penjelasan Struktur:
- **/data**: Direktori ini berisi dataset yang digunakan dalam proyek, dalam format `.csv`.
- **/dashboard**: Direktori ini berisi `dashboard.py` yang digunakan untuk membuat dashboard hasil analisis data.
- **notebook.ipynb**: File ini digunakan untuk melakukan analisis data (EDA) di Google Colab atau Jupyter Notebook.
- **requirements.txt**: Berisi daftar library Python yang diperlukan untuk menjalankan proyek.
- **README.md**: File ini, berisi penjelasan tentang proyek.
- **url.txt**: Berisi tautan (URL) ke dashboard Streamlit.

## Instalasi
1. Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:
   ```bash
   git clone https://github.com/NaufalNurFahriza/data-analyst-python-dicoding.git
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd data-analyst-python-dicoding
   ```

3. Buat dan aktifkan virtual environment (opsional):
   ```bash
   python -m venv myenv
   # Untuk Windows:
   myenv\Scripts\activate
   # Untuk Linux/Mac:
   source myenv/bin/activate
   ```

4. Install library yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan
1. Untuk menjalankan dashboard secara lokal:
   * Masuk ke direktori `dashboard`:
     ```bash
     cd dashboard
     ```

   * Jalankan Streamlit:
     ```bash
     streamlit run dashboard.py
     ```

   * Buka browser dan akses `http://localhost:8501`.

2. Untuk melihat dashboard yang sudah dideploy, kunjungi: https://data-analyst-python-bike-sharing.streamlit.app/

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repository ini dan buat pull request.

## Lisensi
Proyek ini dilisensikan di bawah MIT License.

## Kontak
* Nama: Naufal Nur Fahriza
* Email: naufalnurfahriza@gmail.com
* GitHub: NaufalNurFahriza
