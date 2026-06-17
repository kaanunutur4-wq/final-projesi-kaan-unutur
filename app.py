import streamlit as st
import pandas as pd
import joblib

# Arayüz başlık ve açıklamalarsı
st.title("🥊 UFC Karar Destek Sistemi")
st.write("Kırmızı ve Mavi köşe dövüşçülerinin fiziksel ve istatistiksel verilerini girerek maç sonucunu tahmin edin.")

# Kaydettiğimiz modeli yükleme
model = joblib.load('data/rf_model.pkl')

# Kullanıcı arayüzünü iki sütuna bölüyoruz
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟦 Mavi Köşe")
    b_age = st.number_input("Yaş (Mavi)", min_value=18.0, max_value=60.0, value=28.0)
    b_height = st.number_input("Boy (cm) (Mavi)", min_value=150.0, max_value=220.0, value=175.0)
    b_reach = st.number_input("Uzanma Mesafesi (Mavi)", min_value=150.0, max_value=220.0, value=180.0)
    b_str = st.number_input("Ort. İsabetli Vuruş (Mavi)", min_value=0.0, max_value=200.0, value=30.0)
    b_td = st.number_input("Ort. Takedown (Mavi)", min_value=0.0, max_value=15.0, value=1.0)

with col2:
    st.subheader("🟥 Kırmızı Köşe")
    r_age = st.number_input("Yaş (Kırmızı)", min_value=18.0, max_value=60.0, value=28.0)
    r_height = st.number_input("Boy (cm) (Kırmızı)", min_value=150.0, max_value=220.0, value=175.0)
    r_reach = st.number_input("Uzanma Mesafesi (Kırmızı)", min_value=150.0, max_value=220.0, value=180.0)
    r_str = st.number_input("Ort. İsabetli Vuruş (Kırmızı)", min_value=0.0, max_value=200.0, value=30.0)
    r_td = st.number_input("Ort. Takedown (Kırmızı)", min_value=0.0, max_value=15.0, value=1.0)

st.markdown("---")

# Tahmin İşlemi
if st.button("Sonucu Tahmin Et", use_container_width=True):
    # Kullanıcıdan alınan verileri modelin anlayacağı formata (DataFrame) çeviriyoruz
    girdi_verisi = pd.DataFrame({
        'B_age': [b_age], 'R_age': [r_age],
        'B_Height_cms': [b_height], 'R_Height_cms': [r_height],
        'B_Reach_cms': [b_reach], 'R_Reach_cms': [r_reach],
        'B_avg_SIG_STR_landed': [b_str], 'R_avg_SIG_STR_landed': [r_str],
        'B_avg_TD_landed': [b_td], 'R_avg_TD_landed': [r_td]
    })
    
    # Modelden tahmini ve güven (olasılık) skorunu alma
    tahmin = model.predict(girdi_verisi)[0]
    ihtimal = model.predict_proba(girdi_verisi)[0]
    
    if tahmin == 1:
        st.success(f"🏆 **Tahmin:** Kırmızı Köşe Kazanır! (Güven Skoru: %{ihtimal[1]*100:.1f})")
    else:
        st.info(f"🏆 **Tahmin:** Mavi Köşe Kazanır! (Güven Skoru: %{ihtimal[0]*100:.1f})")