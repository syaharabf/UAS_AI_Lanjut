import streamlit as st
import joblib
import re

# Mengatur tampilan halaman web agar lebih rapi
st.set_page_config(page_title="Analisis Sentimen App", page_icon="📱", layout="centered")

# --- FUNGSI PEMBERSIH TEKS (Wajib sama persis dengan di Colab) ---
def bersihkan_teks(teks):
    teks = str(teks).lower()
    teks = re.sub(r'[^a-z\s]', '', teks)
    teks = teks.strip()
    return teks

# --- LOAD MODEL & VECTORIZER ---
# Menggunakan cache agar model tidak perlu dimuat ulang setiap web di-refresh
@st.cache_resource
def load_model():
    model = joblib.load('model_sentimen_svm.pkl')
    vectorizer = joblib.load('vectorizer_tfidf.pkl')
    return model, vectorizer

model, vectorizer = load_model()

# --- ANTARMUKA WEB ---
st.title("📱 Analisis Sentimen Ulasan")
st.write("Silakan masukkan teks ulasan pengguna di bawah ini untuk melihat apakah ulasan tersebut bersentimen **Positif** atau **Negatif**.")

# Form Input
ulasan_pengguna = st.text_area("Masukkan Ulasan (contoh: 'Aplikasinya lemot banget, susah dipakai'):", height=150)

# Tombol Prediksi
if st.button("Analisis Sentimen 🚀"):
    if ulasan_pengguna.strip() == "":
        st.warning("Mohon masukkan teks ulasan terlebih dahulu.")
    else:
        with st.spinner("Menganalisis..."):
            # 1. Bersihkan teks inputan user
            teks_bersih = bersihkan_teks(ulasan_pengguna)
            
            # 2. Ubah teks menjadi angka menggunakan vectorizer
            teks_vector = vectorizer.transform([teks_bersih])
            
            # 3. Lakukan prediksi dengan model SVM
            prediksi = model.predict(teks_vector)
            
            # 4. Tampilkan Hasil
            st.markdown("---")
            if prediksi[0] == 1:
                st.success("✨ **Hasil: Sentimen Positif**")
                st.write("Pengguna tampaknya puas dengan antarmuka dan layanan aplikasi.")
            else:
                st.error("⚠️ **Hasil: Sentimen Negatif**")
                st.write("Pengguna mengalami kendala atau ketidakpuasan. Interaksi pengguna (UI/UX) mungkin perlu dievaluasi lebih lanjut.")