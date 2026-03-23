import streamlit as st
import matplotlib.pyplot as plt

# Başlık ve Açıklama
st.set_page_config(page_title="GreenBudget AI", page_icon="🌱")
st.title("🌱 GreenBudget AI: Sürdürülebilir Mali Asistan")
st.markdown("""
Bu uygulama, kamu maliyesi ve sürdürülebilirliği birleştirerek harcamalarınızın 
**Karbon Ayak İzini** ve potansiyel **Yeşil Vergi** yükünü hesaplar.
""")

# Kullanıcı Girişleri
st.sidebar.header("Aylık Harcama Verileri")
ulasim = st.sidebar.number_input("Akaryakıt Harcaması (TL)", min_value=0)
elektrik = st.sidebar.number_input("Elektrik Faturası (TL)", min_value=0)
dogalgaz = st.sidebar.number_input("Doğalgaz Faturası (TL)", min_value=0)
su = st.sidebar.number_input("Su Faturası (TL)", min_value=0)
gida = st.sidebar.number_input("Gıda Harcaması (TL)", min_value=0)

# Güncellenmiş Katsayılar (Tahmini değerler)
CO2_ULASIM = 0.0005 
CO2_ELEKTRIK = 0.0004
CO2_DOGALGAZ = 0.0003
CO2_SU = 0.0001
CO2_GIDA = 0.0001
KARBON_VERGI_ORANI = 0.15 # %15 Yeşil Vergi Simülasyonu

# Hesaplamalar
toplam_co2 = (ulasim * CO2_ULASIM) + (elektrik * CO2_ELEKTRIK) + \
             (dogalgaz * CO2_DOGALGAZ) + (su * CO2_SU) + (gida * CO2_GIDA)

potansiyel_vergi = toplam_co2 * KARBON_VERGI_ORANI

# Sonuç Ekranı
col1, col2 = st.columns(2)
with col1:
    st.metric("Tahmini Toplam Karbon", f"{toplam_co2:.2f} kg CO2")
with col2:
    st.metric("Simüle Edilen Yeşil Vergi", f"{potansiyel_vergi
