import pickle
import numpy as np
import streamlit as st
import pandas as pd

# load save model
model = pickle.load(open('penyakit_jantung.sav','rb'))

def main_page():
    st.sidebar.markdown("# Selamat Datang")
    st.title('Selamat Datang Di Web Prediksi Penyakit Jantung')
    st.image('jantung.jpg')

def page2():
    st.sidebar.markdown("# Selamat Mencoba")
    st.title('Prediksi Penyakit Jantung')

    age = st.text_input('Umur')

    sex = st.text_input('Jenis Kelamin')

    cp = st.text_input('Jenis Nyeri Dada')

    trestbps = st.text_input('Tekanan Darah')

    chol = st.text_input('Nilai Kolesterol')

    fbs = st.text_input('Gula Darah')

    restecg = st.text_input('Hasil Elektrokadiografi')

    thalach = st.text_input('Detak Jantung Maksimum')

    exang = st.text_input('Induksi Angina')

    oldpeak = st.text_input('ST Depression')

    slope = st.text_input('Slope')

    ca = st.text_input('Nilai CA')
    
    thal = st.text_input('Nilai Thal')

    # code untuk prediksi
    heart_diagnosis = ''

    # Tombol prediksi
    if st.button('Prediksi Penyakit Jantung'):
        try:
            # Melakukan pengecekan dan konversi ke float
            age = float(age) if age != '' else 0.0
            sex = float(sex) if sex != '' else 0.0
            cp = float(cp) if cp != '' else 0.0
            trestbps = float(trestbps) if trestbps != '' else 0.0
            chol = float(chol) if chol != '' else 0.0
            fbs = float(fbs) if fbs != '' else 0.0
            restecg = float(restecg) if restecg != '' else 0.0
            thalach = float(thalach) if thalach != '' else 0.0
            exang = float(exang) if exang != '' else 0.0
            oldpeak = float(oldpeak) if oldpeak != '' else 0.0
            slope = float(slope) if slope != '' else 0.0
            ca = float(ca) if ca != '' else 0.0
            thal = float(thal) if thal != '' else 0.0

            # Membuat array numpy 2D dari input
            input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            # Melakukan prediksi
            heart_prediction = model.predict(input_data)

            # Menentukan hasil prediksi
            if heart_prediction[0] == 1:
                heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
            else:
                heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'

            st.success(heart_diagnosis)

        except ValueError as e:
            st.error(f"Terjadi kesalahan: {e}. Pastikan semua input berupa angka.")

def page3() :
    df = pd.read_csv('jantung.csv')
    st.write(df)
        
page_names_to_funcs = {
    "Home" : main_page,
    "Test" : page2,
    "Data" : page3,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
