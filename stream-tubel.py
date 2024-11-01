# library
import pickle
import numpy as np
import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# load save model
model = pickle.load(open('penyintas_tubel.sav', 'rb'))
df = pd.DataFrame()

# judl web
st.title('Penyintas Tubel')
st.markdown("Aplikasi prediksi ketepatan waktu lapor setelah kembali dari tugas belajar bagi pegawai tubel")
st.subheader("Identitas Pegawai Tubel")

# Pilihan jenis Kelamin
jenis_kelamin = st.selectbox("Jenis Kelamin:", ("Laki-laki", "Perempuan"))

# Update dataset berdasarkan pilihan
if jenis_kelamin == "Laki-laki":
    df['jenis_kelamin_laki-laki'] = [1]
    df['jenis_kelamin_perempuan'] = [0]
elif jenis_kelamin == "Perempuan":
    df['jenis_kelamin_laki-laki'] = [0]
    df['jenis_kelamin_perempuan'] = [1]

# Pilihan Strata
strata = st.selectbox("Strata:", ("D-3", "D-4/S-1", "S-2", "S-3"))

# Update dataset berdasarkan pilihan
if strata == "D-3":
    df['Strata'] = [0]
elif strata == "D-4/S-1":
    df['Strata'] = [1]
elif strata == "S-2":
    df['Strata'] = [2]
elif strata == "S-3":
    df['Strata'] = [3]


# Pilihan Kluster
kluster = st.selectbox("Kluster Jurursan:", ("Akuntansi", "Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan", "Hukum", "Ilmu Administrasi, Administrasi Pembangunan dan Bisnis", "Kebijakan Publik", "Manajemen, Ilmu Manajemen dan Manajemen Terapan", "SDM, Psikolog, Kepemimpinan dan Komunikasi", "Studi Pembangunan, Ilmu Pembangunan", "TI dan Komputer", "Lainnya"))

# Update dataset berdasarkan pilihan
if kluster == "Akuntansi":
    df['kluster_Akuntansi'] = [1]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [1]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "Hukum":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [1]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "Ilmu Administrasi, Administrasi Pembangunan dan Bisnis":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [1]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "Kebijakan Publik":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [1]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "Manajemen, Ilmu Manajemen dan Manajemen Terapan":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [1]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "SDM, Psikolog, Kepemimpinan dan Komunikasi":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [1]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "Studi Pembangunan, Ilmu Pembangunan":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [1]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [0]
elif kluster == "TI dan Komputer":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [1]
    df['kluster_Lainnya'] = [0]
elif kluster == "Lainnya":
    df['kluster_Akuntansi'] = [0]
    df['kluster_Ekonomi, Ilmu Ekonomi, dan Ekonomi Terapan'] = [0]
    df['kluster_Hukum'] = [0]
    df['kluster_Ilmu Administrasi, Administrasi Pembangunan dan Bisnis'] = [0]
    df['kluster_Kebijakan Publik'] = [0]
    df['kluster_Manajemen, Ilmu Manajemen dan Manajemen Terapan'] = [0]
    df['kluster_SDM, Psikolog, Kepemimpinan dan Komunikasi'] = [0]
    df['kluster_Studi Pembangunan, Ilmu Pembangunan'] = [0]
    df['kluster_TI dan Komputer'] = [0]
    df['kluster_Lainnya'] = [1]


# Pilihan Universitas
universitas = st.selectbox("Universitas:", ("IPB", "ITB", "ITS", "PKN STAN", "UB", "UGM", "UI", "UNAIR", "UNAND", "UNDIP", "UNHAN", "UNHAS", "UNILA", "UNPAD", "UNS", "UNSRI", "UNSUD", "indo_lainnya", "AUS", "JPN", "UK", "USA", "Linkage", "lainnya"))

# Update dataset berdasarkan pilihan
if universitas == "IPB":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [1]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "ITB":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [1]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "ITS":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [1]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "PKN STAN":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [1]
elif universitas == "UB":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [1]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UGM":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [1]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UI":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [1]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNAIR":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [1]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNAND":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [1]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNDIP":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [1]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNHAN":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [1]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNHAS":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [1]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNILA":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [1]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNPAD":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [1]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNS":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [1]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNSRI":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [1]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UNSUD":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [1]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "indo_lainnya":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [1]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "AUS":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [1]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "JPN":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [1]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "UK":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [1]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "USA":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [1]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "Linkage":
    df['univ_lainnya'] = [0]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [1]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]
elif universitas == "lainnya":
    df['univ_lainnya'] = [1]
    df['univ_indo_lainnya'] = [0]
    df['univ_Linkage'] = [0]
    df['univ_USA'] = [0]
    df['univ_ITS'] = [0]
    df['univ_JPN'] = [0]
    df['univ_UNHAN'] = [0]
    df['univ_ITB'] = [0]
    df['univ_UNAIR'] = [0]
    df['univ_UNSRI'] = [0]
    df['univ_IPB'] = [0]
    df['univ_UB'] = [0]
    df['univ_UNDIP'] = [0]
    df['univ_AUS'] = [0]
    df['univ_UNPAD'] = [0]
    df['univ_UGM'] = [0]
    df['univ_UNHAS'] = [0]
    df['univUK'] = [0]
    df['univ_UNILA'] = [0]
    df['univ_UNAND'] = [0]
    df['univ_UI'] = [0]
    df['univ_UNSUD'] = [0]
    df['univ_UNS'] = [0]
    df['univ_PKN STAN'] = [0]


# Pilihan Tahun Intake dengan range 2010 - 2050
tahun_intake = st.number_input(
    'tahun_intake',
    min_value=2010,
    max_value=2050,
    step=1,
    format="%d"
)
df['tahun_intake'] = tahun_intake

# Pilihan Umur dengan range 17 - 60
Umur_intake = st.number_input(
    'Umur_intake',
    min_value=17,
    max_value=60,
    step=1,
    format="%d"
)
df['Umur_intake'] = Umur_intake

# Pilihan Lama Bekerja dengan range 0 - 43
Lama_Bekerja = st.number_input(
    'Lama_Bekerja',
    min_value=0,
    max_value=43,
    step=1,
    format="%d"
)
df['Lama_Bekerja'] = Lama_Bekerja

# Pilihan Sumber Dana
sumber_dana = st.selectbox("Sumber Dana:", ("AAS", "DIPA BPKP", "Kementerian Keuangan RI", "Kementerian Komunikasi dan Informatika RI", "Kementerian Pertahanan RI", "KOICA", "LPDP", "LPPNTB", "New Zealand Aid Programmed Scholarship", "Pusbindiklatren Bappenas", "SPIRIT", "STAR", "Lainnya"))

# Update dataset berdasarkan pilihan
if sumber_dana == "Lainnya":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [1]
elif sumber_dana == "AAS":
    df['AAS'] = [1]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "DIPA BPKP":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [1]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "Kementerian Keuangan RI":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [1]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "Kementerian Komunikasi dan Informatika RI":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [1]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "Kementerian Pertahanan RI":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [1]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "KOICA":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [1]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "LPDP":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [1]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "LPPNTB":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [1]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "New Zealand Aid Programmed Scholarship":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [1]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "Pusbindiklatren Bappenas":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [1]
    df['SPIRIT'] = [0]
    df['STAR'] = [0]
    df['Lainnya'] = [0]
elif sumber_dana == "SPIRIT":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [1]
    df['Lainnya'] = [0]
elif sumber_dana == "STAR":
    df['AAS'] = [0]
    df['DIPA BPKP'] = [0]
    df['Kementerian Keuangan RI'] = [0]
    df['Kementerian Komunikasi dan Informatika RI'] = [0]
    df['Kementerian Pertahanan RI'] = [0]
    df['KOICA'] = [0]
    df['LPDP'] = [0]
    df['LPPNTB'] = [0]
    df['New Zealand Aid Programmed Scholarship'] = [0]
    df['Pusbindiklatren Bappenas'] = [0]
    df['SPIRIT'] = [0]
    df['STAR'] = [1]
    df['Lainnya'] = [0]

# Pilihan Jabatan
jabatan = st.selectbox("Jabatan:", ("Auditor Pelaksana", "Auditor Pertama", "Auditor Muda", "Auditor Madya", "JFU"))

# Update dataset berdasarkan pilihan
if jabatan == "Auditor Pelaksana":
    df['JFU'] = [0]
    df['Sert.Aud.Muda'] = [0]
    df['Sert.Aud.Pelaksana'] = [1]
    df['Sert.Aud.Pertama'] = [0]
    df['auditor_madya'] = [0]
elif jabatan == "Auditor Pertama":
    df['JFU'] = [0]
    df['Sert.Aud.Muda'] = [0]
    df['Sert.Aud.Pelaksana'] = [0]
    df['Sert.Aud.Pertama'] = [1]
    df['auditor_madya'] = [0]
elif jabatan == "Auditor Muda":
    df['JFU'] = [0]
    df['Sert.Aud.Muda'] = [1]
    df['Sert.Aud.Pelaksana'] = [0]
    df['Sert.Aud.Pertama'] = [0]
    df['auditor_madya'] = [0]
elif jabatan == "Auditor Madya":
    df['JFU'] = [0]
    df['Sert.Aud.Muda'] = [0]
    df['Sert.Aud.Pelaksana'] = [0]
    df['Sert.Aud.Pertama'] = [0]
    df['auditor_madya'] = [1]
elif jabatan == "JFU":
    df['JFU'] = [1]
    df['Sert.Aud.Muda'] = [0]
    df['Sert.Aud.Pelaksana'] = [0]
    df['Sert.Aud.Pertama'] = [0]
    df['auditor_madya'] = [0]


# Pilihan Pasangan
pasangan = st.selectbox("Pasangan:", ("Lajang", "BPKP", "Non BPKP"))

# Update dataset berdasarkan pilihan
if pasangan == "Lajang":
    df['lajang'] = [1]
    df['pasangan_BPKP'] = [0]
    df['pasangan_NonBPKP'] = [0]
elif pasangan == "BPKP":
    df['lajang'] = [0]
    df['pasangan_BPKP'] = [1]
    df['pasangan_NonBPKP'] = [0]
elif pasangan == "Non BPKP":
    df['lajang'] = [0]
    df['pasangan_BPKP'] = [0]
    df['pasangan_NonBPKP'] = [1]

# Pilihan DOmisili
domisili = st.selectbox("Universitas termasuk Domisili:", ("Ya", "Tidak"))

# Update dataset berdasarkan pilihan
if domisili == "Ya":
    df['domisili'] = [1]
    df['tidak_domisili'] = [0]
elif domisili == "Tidak":
    df['domisili'] = [0]
    df['tidak_domisili'] = [1]

# Tampilkan hasil dataset
st.write("Data yang diinput:")
st.write(df)

# model prodiksi
prediksi_tubel =''

# Membuat tombol prediksi
if st.button('Prediksi Keterlambatan'):
    prediksi_tubel = model.predict(df.to_numpy())

    if (prediksi_tubel[0]==1):
        prediksi_tubel = 'Terlambat'
    else:
        prediksi_tubel = 'Tidak Terlambat'

st.success(prediksi_tubel)