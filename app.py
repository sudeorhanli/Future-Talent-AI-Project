import streamlit as st

# Başlık ve Açıklama
st.set_page_config(page_title="GreenBudget AI", page_icon="🌱")
st.title("🌱 GreenBudget AI: Sürdürülebilir Mali Asistan")
st.markdown("""
Bu uygulama, kamu maliyesi ve sürdürülebilirliği birleştirerek harcamalarınızın 
**Karbon Ayak İzini** ve potansiyel **Yeşil Vergi** yükünü hesaplar.
""")

# Kullanıcı Girişleri
st.sidebar.header("Harcama Verileri")
ulasim = st.sidebar.number_input("Aylık Akaryakıt Harcaması (TL)", min_value=0)
elektrik = st.sidebar.number_input("Aylık Elektrik Faturası (TL)", min_value=0)
gida = st.sidebar.number_input("Aylık Gıda Harcaması (TL)", min_value=0)

# Basit Katsayılar (Örnek Değerler)
# 1 TL harcama başına kg CO2 salınımı tahmini
CO2_ULASIM = 0.0005 
CO2_ENERJI = 0.0003
CO2_GIDA = 0.0001
KARBON_VERGI_ORANI = 0.15 # %15 Yeşil Vergi Simülasyonu

# Hesaplamalar
toplam_co2 = (ulasim * CO2_ULASIM) + (elektrik * CO2_ENERJI) + (gida * CO2_GIDA)
potansiyel_vergi = toplam_co2 * KARBON_VERGI_ORANI

# Sonuç Ekranı
col1, col2 = st.columns(2)
with col1:
    st.metric("Tahmini Karbon Salınımı", f"{toplam_co2:.2f} kg CO2")
with col2:
    st.metric("Simüle Edilen Yeşil Vergi", f"{potansiyel_vergi:.2f} TL")

st.divider()

# AI Tavsiyesi (Kural Tabanlı Mantık)
st.subheader("🤖 AI Sürdürülebilirlik Tavsiyesi")
if toplam_co2 > 10:
    st.warning("Karbon ayak iziniz yüksek! Ulaşım harcamalarınızı azaltmak bütçenize ve doğaya katkı sağlar.")
else:
    st.success("Tebrikler! Düşük karbonlu bir tüketim alışkanlığınız var.")

st.info("Bu proje Future Talent Program 201 Bitirme Projesi olarak geliştirilmiştir.")
