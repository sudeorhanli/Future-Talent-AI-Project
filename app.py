import streamlit as st
import matplotlib.pyplot as plt

# Sayfa Ayarları
st.set_page_config(page_title="GreenBudget AI", page_icon="🌱")

# Ana Başlık
st.title("🌿 GreenBudget AI: Sürdürülebilir Mali Asistan")
st.markdown("""
Kamu Maliyesi disiplini ile yapay zekayı birleştirerek harcamalarınızın **Karbon Ayak İzini** ve potansiyel **Yeşil Vergi** yükünü hesaplar.
""")

# Yan Menü
st.sidebar.header("💳 Aylık Harcama Verileri")
ulasim = st.sidebar.number_input("Akaryakıt Harcaması (TL)", min_value=0)
elektrik = st.sidebar.number_input("Elektrik Faturası (TL)", min_value=0)
dogalgaz = st.sidebar.number_input("Doğalgaz Faturası (TL)", min_value=0)
su = st.sidebar.number_input("Su Faturası (TL)", min_value=0)
gida = st.sidebar.number_input("Gıda Harcaması (TL)", min_value=0)

# Hesaplamalar
CO2_ULASIM, CO2_ELEKTRIK, CO2_DOGALGAZ, CO2_SU, CO2_GIDA = 0.0005, 0.0004, 0.0003, 0.0001, 0.0001
toplam_co2 = (ulasim * CO2_ULASIM) + (elektrik * CO2_ELEKTRIK) + (dogalgaz * CO2_DOGALGAZ) + (su * CO2_SU) + (gida * CO2_GIDA)
potansiyel_vergi = toplam_co2 * 0.15

# Sonuç Metrikleri
col1, col2 = st.columns(2)
with col1:
    st.subheader("🏭 Toplam Karbon")
    st.metric("", f"{toplam_co2:.2f} kg CO2")
with col2:
    st.subheader("🏛️ Yeşil Vergi")
    st.metric("", f"{potansiyel_vergi:.2f} TL")

st.divider()

# Grafik Bölümü
if toplam_co2 > 0:
    st.subheader("📊 Karbon Kaynaklarınızın Dağılımı")
    labels = ['Ulaşım', 'Elektrik', 'Doğalgaz', 'Su', 'Gıda']
    values = [ulasim * CO2_ULASIM, elektrik * CO2_ELEKTRIK, dogalgaz * CO2_DOGALGAZ, su * CO2_SU, gida * CO2_GIDA]
    f_vals = [v for v in values if v > 0]
    f_labs = [labels[i] for i, v in enumerate(values) if v > 0]
    
    if f_vals:
        fig, ax = plt.subplots()
        ax.pie(f_vals, labels=f_labs, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)

# Tavsiye Bölümü
st.subheader("💡 AI Sürdürülebilirlik Tavsiyesi")
if toplam_co2 > 15:
    st.warning("Karbon ayak iziniz yüksek! Tasarruf önlemleri almanız önerilir.")
elif toplam_co2 > 0:
    st.success("Harika! Sürdürülebilir bir tüketim dengesi kurmuşsunuz.")
else:
    st.info("Hesaplama için veri girişi yapınız.")

st.divider()
st.caption("Future Talent Program 201 - AI Bitirme Projesi")
