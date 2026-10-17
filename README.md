# Judul Project

## Repository Outline
1. `notebook.ipynb` - Notebook ini adalah notebook utama yang berisi proses EDA, Feature Engineering, Model, Evaluasi dan Tuning.
2. `notebook_inf.ipynb` - Notebook ini untuk melakukan inference menggunakan data baru.
3. `bank-addition.csv` - Dataset yang digunakan dalam pembuatan model.
4. `model.pkl` - Best Model yaitu Random Forest.
5. `windsoriser.pkl` - Winsorizer yang digunakan untuk handling outlier.
6. `label-encoder.pkl` - Label Encoder untuk mengubah target menjadi 1 dan 0.
7. `src/eda.py` - Menampilkan halaman yang berisi visualisasi data di Streamlit.
8. `src/prediction.py` - Menampilkan halaman form untuk prediksi di Streamlit.
9. `src/streamlit_app.py` - Menampilkan gabungan halaman eda dan prediction di Streamlit.
10. `requirements.txt` - Daftar library yang dibutuhkan.

## Problem Background
Kampanye pemasaran bank sering melakukan panggilan telpon dengan calon nasabah. Tapi menghubungi calon nasabah tanpa mengetahui kemungkinan mereka akan berlangganan deposit atau tidak akan sangat memakan waktu, biaya dan sumber daya manusia.

Oleh karena itu diperlukan sebuah model untuk memprediksi apakah calon nasabah yang akan dihubungi itu akan berlangganan deposito atau tidak dari data diri calon nasabah tersebut. Sehingga model ini dapat membantu bank dalam menghemat waktu, biaya dan sumber daya manusia.

## Project Output
Output project ini adalah prediksi calon nasabah apakah akan berlangganan deposito atau tidak.

## Data
Dataset yang digunakan adalah `bank-additional.csv` terdiri dari 4.119 baris data dan 21 kolom. Dataset ini berisi informasi mengenai calon nasabah, riwayat dari pemasaran deposito dengan calon nasabah dan keputusan nasabah untuk berlangganan deposito. Dataset ini tidak memiliki data duplikat dan missing value. Nilai 999 pada pdays diubah menjadi missing value karena berarti nasabah belum pernah dihubungi sebelumnya. Lalu target pada dataset ini (y) itu tidak seimbang, sekitar 89% nilainya no dan sekitar 11% nilainya yes.

## Method
Project ini menggunakan metode Supervised Learning untuk klasifikasi. Model yang dibandingkan ada 5 yaitu : KNN, SVM, Decision Tree, Random Forest dan XGBoost.

## Stacks
Stacks yang digunakan : Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Imbalanced-learn, Feature-engine, Streamlit dan Pickle.

## Reference
URL Dataset (Pilih yang bank-additional.csv): https://archive.ics.uci.edu/dataset/222/bank+marketing

URL Model : https://drive.google.com/drive/folders/1aqmGzsxamUHuaTQxc1yCumPAT9FPDSrL?usp=sharing

URL Streamlit : https://deposit-prediction-portugal.streamlit.app/

---