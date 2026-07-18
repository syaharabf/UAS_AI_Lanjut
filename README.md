# UAS_AI_Lanjut

## 1. Bahasa Pemrograman yang Digunakan
- Python 3

## 2. Framework, Library, API, dkk yang Digunakan
- **Streamlit**: Untuk membangun antarmuka web (*frontend*).
- **Scikit-Learn**: Untuk pemodelan *Machine Learning* (algoritma Support Vector Machine / LinearSVC) dan ekstraksi fitur teks (*TF-IDF Vectorizer*).
- **Pandas & NumPy**: Untuk manipulasi, analisis, dan *preprocessing* data.
- **Joblib**: Untuk menyimpan dan memuat (*load*) model AI ke dalam aplikasi web.
- **Re (Regular Expression)**: Untuk pembersihan teks (*text cleaning*).

## 3. Fungsi dan Fitur Proyek yang Dibangun
- **Analisis Sentimen Otomatis**: Pengguna dapat memasukkan teks ulasan dan sistem akan langsung mengklasifikasikannya sebagai ulasan bersentimen **Positif** atau **Negatif**.
- **Evaluasi UI/UX**: Aplikasi ini dirancang sebagai alat bantu komputasional untuk mengevaluasi tingkat kepuasan pengguna, kendala *usability*, dan interaksi pengguna terhadap suatu platform berdasarkan *feedback* ulasan mereka.

## 4. Kelebihan Proyek yang Dibangun
- **Cepat dan Ringan**: Menggunakan algoritma klasifikasi SVM yang sangat efisien untuk menangani data teks berdimensi tinggi (*TF-IDF*) tanpa memerlukan komputasi berat seperti *Deep Learning*.
- **Akurasi Baik**: Model memiliki akurasi mencapai 84.88% pada data pengujian (*testing*).
- **Antarmuka Interaktif**: Diimplementasikan menggunakan framework Streamlit sehingga UI terlihat bersih, responsif, dan mudah digunakan.

## 5. Kekurangan Proyek yang Dibangun (Bug/Warning)
- **Keterbatasan Pemahaman Konteks**: Model belum sepenuhnya mampu mendeteksi gaya bahasa kompleks seperti sarkasme atau ironi.
- **Kosakata Tidak Baku (Slang)**: Jika pengguna memasukkan kata gaul, singkatan baru, atau salah ketik (*typo*) parah yang tidak pernah dipelajari model dalam dataset pelatihan, akurasi prediksi dapat menurun.

## 6. Dataset (LINK)
- [TikTok App Reviews - Indonesia (Kaggle)](https://www.kaggle.com/datasets/pandaa12/tiktok-app-reviews-indonesia-google-play-store)

## 7. Penjelasan Dataset
Dataset yang digunakan berisi 100.000 ulasan riil pengguna terhadap aplikasi TikTok di Google Play Store. Data ini digunakan untuk melatih model agar memahami pola bahasa pelanggan. Fokus utama pemrosesan berada pada dua kolom:
- **Ulasan**: Berisi teks *feedback* dari pengguna terkait pengalaman dan kepuasan mereka.
- **Rating**: Berisi penilaian bintang (1-5). Untuk kebutuhan klasifikasi biner, data dikonversi menjadi dua kelas sentimen: Rating 1-2 dilabeli sebagai Sentimen Negatif (0), dan Rating 4-5 dilabeli sebagai Sentimen Positif (1). Rating 3 diabaikan dari proses *training* agar model memiliki batas keputusan kelas yang lebih tegas.
