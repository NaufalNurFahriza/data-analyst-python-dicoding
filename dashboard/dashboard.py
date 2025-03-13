import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("🚴️ Dashboard Analisis Data Bike Sharing")

# Sidebar untuk informasi pribadi
st.sidebar.title("Proyek Akhir: Analisis Data Bike Sharing")
st.sidebar.write("Nama: Naufal Nur Fahriza")
st.sidebar.write("Email: naufalnurfahriza@gmail.com")
st.sidebar.write("ID Laskar AI: a297ybf370")

# Fungsi untuk memuat dataset
@st.cache_data
def load_data():
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

# Menambahkan fitur interaktif di sidebar
st.sidebar.header("Filter Data")
min_date = df_day['dteday'].min()
max_date = df_day['dteday'].max()
start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter data berdasarkan rentang tanggal
df_day_filtered = df_day[(df_day['dteday'] >= pd.to_datetime(start_date)) & 
                        (df_day['dteday'] <= pd.to_datetime(end_date))]
df_hour_filtered = df_hour[(df_hour['dteday'] >= pd.to_datetime(start_date)) & 
                        (df_hour['dteday'] <= pd.to_datetime(end_date))]

# Pertanyaan 1: Penyewaan Sepeda per Jam
st.header("📊 Pertanyaan 1: Penyewaan Sepeda per Jam")
hourly_rentals = df_hour_filtered.groupby('hr')['cnt'].sum().reset_index()

# Visualisasi
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

# Barplot untuk jam dengan penyewaan terbanyak
sns.barplot(
    x="hr", 
    y="cnt", 
    data=hourly_rentals.sort_values(by="cnt", ascending=False).head(5), 
    palette=["#FFDF00", "#FFCC00", "#ECBD00", "#CC9900", "#B8860B"], 
    ax=ax[0]
)
ax[0].set_xlabel("Jam (24 Jam)", fontsize=12)
ax[0].set_title("5 Jam dengan Penyewaan Sepeda Terbanyak", fontsize=14)

# Barplot untuk jam dengan penyewaan tersedikit
sns.barplot(
    x="hr", 
    y="cnt", 
    data=hourly_rentals.sort_values(by="cnt", ascending=True).head(5), 
    palette=["#FFDF00", "#FFCC00", "#ECBD00", "#CC9900", "#B8860B"], 
    ax=ax[1]
)
ax[1].set_xlabel("Jam (24 Jam)", fontsize=12)
ax[1].set_title("5 Jam dengan Penyewaan Sepeda Tersedikit", fontsize=14)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()

st.pyplot(fig)

# Pertanyaan 2: Pengaruh Suhu terhadap Peminjaman Sepeda
st.header("🌡️ Pertanyaan 2: Pengaruh Suhu terhadap Penyewaan Sepeda")

# Membuat kategori suhu
temp_bins = [0, 0.25, 0.5, 0.75, 1.0]
temp_labels = ['Sangat Rendah', 'Rendah', 'Sedang', 'Tinggi']
df_day_filtered['temp_category'] = pd.cut(df_day_filtered['temp'], bins=temp_bins, labels=temp_labels)

# Visualisasi
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x="temp_category", y="cnt", data=df_day_filtered, palette="Blues", ci=None)
ax2.set_xlabel("Kategori Suhu", fontsize=12)
ax2.set_ylabel("Rata-rata Jumlah Penyewaan", fontsize=12)
ax2.set_title("Pengaruh Suhu terhadap Penyewaan Sepeda", fontsize=14)

st.pyplot(fig2)

# Menampilkan tabel penyewaan berdasarkan kategori suhu
st.write("### Rata-rata Penyewaan Berdasarkan Kategori Suhu")
temp_category_rentals = df_day_filtered.groupby('temp_category')['cnt'].mean().reset_index()
st.write(temp_category_rentals)
