import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("🚴‍♂️ Bike Sharing Dashboard")

# Sidebar untuk memilih dataset
st.sidebar.header("Pengaturan Dataset")
dataset_choice = st.sidebar.selectbox(
    "Pilih Dataset:",
    ["Hourly Data", "Daily Data"]
)

# Fungsi untuk memuat dataset
@st.cache_data
def load_data(dataset_choice):
    if dataset_choice == "Hourly Data":
        path = "data/hour.csv"  # Path ke dataset per jam
    else:
        path = "data/day.csv"  # Path ke dataset harian
    data = pd.read_csv(path)
    return data

# Memuat dataset
df = load_data(dataset_choice)

# Menampilkan dataset
st.subheader("🔍 Data Awal")
st.write(df.head())

# Statistik Deskriptif
st.subheader("📈 Statistik Singkat")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Data", value=df.shape[0])
with col2:
    st.metric(label="Jumlah Kolom", value=df.shape[1])
with col3:
    st.metric(label="Rata-rata Penyewaan", value=f"{df['cnt'].mean():.2f}")

# Visualisasi Data
st.subheader("📊 Visualisasi Data")
visualization_choice = st.selectbox(
    "Pilih Visualisasi:",
    ["Penyewaan Sepeda per Jam", "Pengaruh Suhu terhadap Penyewaan Sepeda"]
)

if visualization_choice == "Penyewaan Sepeda per Jam":
    st.write("### Penyewaan Sepeda per Jam")
    hourly_rentals = df.groupby('hr')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='hr', y='cnt', data=hourly_rentals, ax=ax, palette="viridis")
    ax.set_xlabel("Jam (0-23)")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Penyewaan Sepeda per Jam")
    st.pyplot(fig)

elif visualization_choice == "Pengaruh Suhu terhadap Penyewaan Sepeda":
    st.write("### Pengaruh Suhu terhadap Penyewaan Sepeda")
    # Membuat kategori suhu
    df['temp_category'] = pd.cut(df['temp'], bins=[0, 0.25, 0.5, 0.75, 1.0], labels=["Very Low", "Low", "Moderate", "High"])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='temp_category', y='cnt', data=df, ax=ax, palette="coolwarm")
    ax.set_xlabel("Kategori Suhu")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Pengaruh Suhu terhadap Penyewaan Sepeda")
    st.pyplot(fig)

# Filter Data
st.subheader("🎯 Filter Data")
with st.expander("Filter Berdasarkan Hari"):
    selected_day = st.selectbox("Pilih Hari:", df["weekday"].unique())
    filtered_data = df[df["weekday"] == selected_day]
    st.write(filtered_data)

with st.expander("Filter Berdasarkan Musim"):
    selected_season = st.selectbox("Pilih Musim:", df["season"].unique())
    filtered_data = df[df["season"] == selected_season]
    st.write(filtered_data)