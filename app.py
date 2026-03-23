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

# Güncellenmiş Katsayılar
CO2_ULASIM = 0.0005 
CO2_ELEKTRIK = 0.0004
CO2_DOGALGAZ = 0.0003
CO2_SU = 0.0001
CO2_GIDA = 0.0001
KARBON_VERGI_ORANI = 0.15

# Hesaplamalar
toplam_co2 = (ulasim * CO2_ULASIM) + (elektrik * CO2_ELEKTRIK) + \
             (dogalgaz * CO2_DOGALGAZ) + (su * CO2_SU) + (gida * CO2_GIDA)

potansiyel_vergi = toplam_co2 * KARBON_VERGI_ORANI

# Sonuç Ekranı
col1, col2 = st.columns(2)
with col1:
    st.metric("Tahmini Toplam Karbon", f"{toplam_co2:.2f} kg CO2")
with col2:
    st.metric("Simüle Edilen Yeşil Vergi", f"{potansiyel_vergi:.2f} TL")

st.divider()

# 🔥 Görselleştirme Katmanı (Sıfır Değerleri Filtreleyen Pasta Grafiği)
if toplam_co2 > 0:
    st.subheader("📊 Karbon Kaynaklarınızın Dağılımı")
    
    # Tüm kategorileri ve emisyonlarını hazırla
    tum_kategoriler = ['Ulaşım', 'Elektrik', 'Doğalgaz', 'Su', 'Gıda']
    tum_emisyonlar = [ulasim * CO2_ULASIM, elektrik * CO2_ELEKTRIK, dogalgaz * CO2_DOGALGAZ, su * CO2_SU, gida * CO2_GIDA]
    tum_renkler = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

    # 🚀 Sadece emisyonu 0'dan büyük olanları seç (Filtreleme)
    aktif_veriler = []
    aktif_etiketler = []
    aktif_renkler = []

    for idx, emisyon in enumerate(tum_emisyonlar):
        if emisyon > 0:
            aktif_veriler.append(emisyon)
            aktif_etiketler.append(tum_kategoriler[idx])
            aktif_renkler.append(tum_renkler[idx])
    
    # Sadece aktif veri varsa grafiği çiz
    if aktif_veriler:
        fig1, ax1 = plt.subplots()
        # labeldistance: Etiketlerin pastadan uzaklığı, autopct: Yüzde formatı, pctdistance: Yüzdelerin pastadan uzaklığı
        ax1.pie(aktif_veriler, labels=aktif_etiketler, autopct='%1.1f%%', 
                startangle=90, colors=aktif_renkler, 
                labeldistance=1.1, pctdistance=0.85)
        ax1.axis('equal') 
        
        # Pasta grafiğinin ortasına beyaz bir daire çizerek simit grafiğine (Donut Chart) çevirelim (Daha okunaklı olur)
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig1.gca().add_artist(centre_circle)
        
        st.pyplot(fig1)

# AI Tavsiyesi
st.subheader("🤖 AI Sürdürülebilirlik Tavsiyesi")
if toplam_co2 > 15:
    st.warning("Karbon ayak iziniz ortalamanın üzerinde! En büyük kaynağı bulup tasarrufa başlayın.")
elif toplam_co2 > 0:
    st.success("Harika! Sürdürülebilir bir tüketim dengesi kurmuşsunuz.")
else:
    st.info("Lütfen hesaplama yapmak için verilerinizi giriniz.")

st.info("Bu proje Future Talent Program 201 Bitirme Projesi olarak geliştirilmiştir.")
