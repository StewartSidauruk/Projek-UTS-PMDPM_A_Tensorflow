import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os

from streamlit_option_menu import option_menu

# Navigasi sidebar
with st.sidebar:
    selected = option_menu ('Kelompok Tensorflow UTS ML 24/25',
                            ['Klasifikasi',
                            'Regresi'],
                            default_index=0)


# Halaman Klasifikasi
if selected == 'Klasifikasi':
    st.title('Klasifikasi')
    #input file
    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("Masukkan File", type=["csv"] )

    model_directory = r'D:\Download 4\ML_UTS\ML_UTS'
    model_path = os.path. join(model_directory, r'BestModel_CLF_GradientBoostingTrees_Tensorflow.pkl')

    with open(model_path,'rb') as f:
            loaded_model = pickle.load(f)

    GBT_model = loaded_model

    #input squaremeters
    squaremeters = st.number_input("Inputkan berapa meter persegi dari properti", 1)
    #input numberofrooms
    st.write ('Inputkan berapa banyak ruangan properti')
    numberofrooms = st.slider ("Ruangan",0,100)
    #input hasyard
    st.write('Apakah properti memiliki halaman?')
    hasyard = st.radio("Halaman",["Ada", "Tidak ada"] )
    #input haspool
    st.write('Apakah properti memiliki kolam?')
    haspool = st.radio("Kolam",["Ada", "Tidak ada"] )
    #input floors
    st.write ('Inputkan berapa banyak lantai dari properti')
    floors = st.slider ("Lantai",0,100)
    #input city-code
    citycode = st.number_input("Inputkan kode pos dari properti", 0)
    #input citypartrange
    st.write ('Inputkan bagian kota jangkauan dari properti')
    citypartrange = st.slider ("jangkauan",1,10)
    #input numprevowners
    st.write ('Inputkan berapa banyak pemilik sebelumnya dari properti')
    numprevowners = st.slider ("pemilik sebelumnya",1,10)
    #input made
    st.write ('Inputkan tahun pembuatan dari properti')
    made = st.slider ("tahun pembuatan",1950,2050)
    #isnewbuilt
    isnewbuilt = st.radio("Bangunan baru",["Tua", "Baru"] )
    #hasstormprotector
    hasstromprotector = st.radio("Penangkal petir",["Ada", "Tidak ada"] )
    #basement
    basement = st.number_input("Banyaknya ruang bawah tanah", 0)
    #Attic
    attic = st.number_input("Banyaknya Loteng", 0)
    #garage
    garage = st.number_input("Masukan jumlah garasi", 0)
    #hasstorageroom
    hasstorageroom = st.radio("Gudang",["Ada", "Tidak ada"] )
    #hasguestroom
    hasguestroom = st.slider("Masukan jumlah ruang tamu",0,10)
    #Input Category
    # nama_kolom = st.selectbox("Kategori",["Mewah", "Menegah", "Biasa"] )
   
    if hasyard == "Ada":
        input_hasyard_yes = 1
        input_hasyard_no = 0
    else:
        input_hasyard_yes = 0
        input_hasyard_no = 1

    if haspool == "Ada":
        input_haspool_yes = 1
        input_haspool_no = 0
    else:
        input_haspool_yes = 0
        input_haspool_no = 1

    if isnewbuilt == "Baru":
        input_isnewbuilt_new = 1
        input_isnewbuilt_old = 0
    else:
        input_isnewbuilt_new = 0
        input_isnewbuilt_old = 1

    if hasstromprotector == "Ada":
        input_hasstormprotector_yes = 1
        input_hasstormprotector_no = 0
    else:
        input_hasstormprotector_yes = 0
        input_hasstormprotector_no = 1

    if hasstorageroom == "Ada":
        input_hasstorageroom_yes = 1
        input_hasstorageroom_no = 0
    else:
        input_hasstorageroom_yes = 0
        input_hasstorageroom_no = 1

    input_data = [[input_hasyard_no, input_hasyard_yes, input_haspool_no, input_haspool_yes, input_isnewbuilt_new, 
                   input_isnewbuilt_old, input_hasstormprotector_no, input_hasstormprotector_yes, input_hasstorageroom_no,
                   input_hasstorageroom_yes, squaremeters, numberofrooms, floors, citycode, citypartrange, numprevowners, made, basement,
                   attic, garage, hasguestroom]]

    if st.button("Prediksi"):
        GBT_model_prediction = GBT_model.predict(input_data)
        outcome= {'Luxury':'Mewah', 'Middle':'Menengah', 'Basic':'Biasa'}
        st.write(f"Properti tersebut diprediksi * {outcome[GBT_model_prediction[0]]} * ")

# Halaman Regresi
if selected == 'Regresi':
    st.title('Regresi')
    #input file
    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("Masukkan File", type=["csv"] )

    model_directory = r'D:\Download 4\ML_UTS\ML_UTS'
    model_path = os.path. join(model_directory, r'BestModel_REG_RidgeRegression_Tensorflow.pkl')

    with open(model_path,'rb') as f:
            loaded_model = pickle.load(f)

    RR_model = loaded_model

    #input squaremeters
    squaremeters = st.number_input("Inputkan berapa meter persegi dari properti", 1)
    #input numberofrooms
    st.write ('Inputkan berapa banyak ruangan properti')
    numberofrooms = st.slider ("Ruangan",0,100)
    #input hasyard
    st.write('Apakah properti memiliki halaman?')
    hasyard = st.radio("Halaman",["Ada", "Tidak ada"] )
    #input haspool
    st.write('Apakah properti memiliki kolam?')
    haspool = st.radio("Kolam",["Ada", "Tidak ada"] )
    #input floors
    st.write ('Inputkan berapa banyak lantai dari properti')
    floors = st.slider ("Lantai",0,100)
    #input city-code
    citycode = st.number_input("Inputkan kode pos dari properti", 0)
    #input citypartrange
    st.write ('Inputkan bagian kota jangkauan dari properti')
    citypartrange = st.slider ("jangkauan",1,10)
    #input numprevowners
    st.write ('Inputkan berapa banyak pemilik sebelumnya dari properti')
    numprevowners = st.slider ("pemilik sebelumnya",1,10)
    #input made
    st.write ('Inputkan tahun pembuatan dari properti')
    made = st.slider ("tahun pembuatan",1950,2050)
    #isnewbuilt
    isnewbuilt = st.radio("Bangunan baru",["Tua", "Baru"] )
    #hasstormprotector
    hasstromprotector = st.radio("Penangkal petir",["Ada", "Tidak ada"] )
    #basement
    basement = st.number_input("Banyaknya ruang bawah tanah", 0)
    #Attic
    attic = st.number_input("Banyaknya Loteng", 0)
    #garage
    garage = st.number_input("Masukan jumlah garasi", 0)
    #hasstorageroom
    hasstorageroom = st.radio("Gudang",["Ada", "Tidak ada"] )
    #hasguestroom
    hasguestroom = st.slider("Masukan jumlah ruang tamu",0,10)

    if hasyard == "Ada":
        input_hasyard_yes = 1
        input_hasyard_no = 0
    else:
        input_hasyard_yes = 0
        input_hasyard_no = 1

    if haspool == "Ada":
        input_haspool_yes = 1
        input_haspool_no = 0
    else:
        input_haspool_yes = 0
        input_haspool_no = 1

    if isnewbuilt == "Baru":
        input_isnewbuilt_new = 1
        input_isnewbuilt_old = 0
    else:
        input_isnewbuilt_new = 0
        input_isnewbuilt_old = 1

    if hasstromprotector == "Ada":
        input_hasstormprotector_yes = 1
        input_hasstormprotector_no = 0
    else:
        input_hasstormprotector_yes = 0
        input_hasstormprotector_no = 1

    if hasstorageroom == "Ada":
        input_hasstorageroom_yes = 1
        input_hasstorageroom_no = 0
    else:
        input_hasstorageroom_yes = 0
        input_hasstorageroom_no = 1

    input_data = [[input_hasyard_no, input_hasyard_yes, input_haspool_no, input_haspool_yes, input_isnewbuilt_new, input_isnewbuilt_old,
                   input_hasstormprotector_no, input_hasstormprotector_yes, input_hasstorageroom_no, input_hasstorageroom_yes,
                   squaremeters,numberofrooms, floors, citycode, citypartrange, numprevowners, made, basement, attic, garage, hasguestroom]]

    if st.button("Prediksi"):
        RR_model_prediction = RR_model.predict(input_data)
        st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Prediksi harga properti adalah: Rp. {RR_model_prediction[0]:.2f}</h3>", unsafe_allow_html=True)
    else:
        st.error("Model tidak ditemukan, silakan cek file model di direktori.")
