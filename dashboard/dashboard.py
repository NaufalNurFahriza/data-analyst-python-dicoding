import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("🚴‍♂️ Dashboard Analisis Data Bike Sharing")

# Sidebar untuk informasi pribadi
st.sidebar.title("Proyek Akhir: Analisis Data Bike Sharing")
st.sidebar.write("Nama: Naufal Nur Fahriza")
st.sidebar.write("Email: naufalnurfahriza@gmail.com")
st.sidebar.write("ID Laskar AI: a297ybf370")

# Fungsi untuk memuat dataset
@st.cache_data
def load_data():
    # Mengimpor dataset dari GitHub
    url_day = "https://raw.githubusercontent.com/NaufalNurFahriza/data-analyst-python-dicoding/main/data/day.csv"
    url_hour = "https://raw.githubusercontent.com/NaufalNurFahriza/data-analyst-python-dicoding/main/data/hour.csv"
    df_day = pd.read_csv(url_day)
    df_hour = pd.read_csv(url_hour)
    return df_day, df_hour

# Memuat dataset
df_day, df_hour = load_data()

# Membersihkan dan memproses data
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

# Membuat kategori suhu
temp_bins = [0, 0.25, 0.5, 0.75, 1.0]
temp_labels = ['Very Low', 'Low', 'Moderate', 'High']
df_day['temp_category'] = pd.cut(df_day['temp'], bins=temp_bins, labels=temp_labels)

# Pertanyaan 1: Pada jam berapa penyewaan sepeda yang paling banyak dan paling sedikit?
st.header("📊 Pertanyaan 1: Penyewaan Sepeda per Jam")
hourly_rentals = df_hour.groupby('hr')['cnt'].sum().reset_index()

# Visualisasi untuk Pertanyaan 1
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='hr', y='cnt', data=hourly_rentals, ax=ax1, palette="viridis")
ax1.set_xlabel("Jam (0-23)")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Penyewaan Sepeda per Jam")
st.pyplot(fig1)

# Menampilkan jam dengan penyewaan terbanyak dan terdikit
st.write("### Jam dengan Penyewaan Terbanyak")
st.write(hourly_rentals.sort_values('cnt', ascending=False).head())

st.write("### Jam dengan Penyewaan Terdikit")
st.write(hourly_rentals.sort_values('cnt', ascending=True).head())

# Pertanyaan 2: Bagaimana pengaruh suhu terhadap peminjaman sepeda?
st.header("🌡️ Pertanyaan 2: Pengaruh Suhu terhadap Penyewaan Sepeda")

# Visualisasi untuk Pertanyaan 2
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='temp_category', y='cnt', data=df_day, ax=ax2, palette="coolwarm")
ax2.set_xlabel("Kategori Suhu")
ax2.set_ylabel("Jumlah Penyewaan")
ax2.set_title("Pengaruh Suhu terhadap Penyewaan Sepeda")
st.pyplot(fig2)

# Menampilkan rata-rata penyewaan berdasarkan kategori suhu
st.write("### Rata-rata Penyewaan Berdasarkan Kategori Suhu")
temp_category_rentals = df_day.groupby('temp_category')['cnt'].mean().reset_index()
st.write(temp_category_rentals)