import streamlit as st
import matplotlib.pyplot as plt
import requests
from streamlit_lottie import st_lottie # 🔥 Lottie desteği

# --- Fonksiyonlar ---
# Lottie animasyonunu internetten çekmek için
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Sayfa Ayarları ---
st.set_page_config(
    page_title="GreenBudget AI",
    page_icon=":leaf:", # Streamlit'in kendi ikon kütüphanesinden
    layout="wide" # Sayfayı genişletelim
)

# --- İkonları Yükle ---
# Sürdürülebilirlik animasyonu (Ana Başlık İçin)
lottie_sustainability = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tlj5g4g1.json") 
# AI asistan animasyonu (Tavsiye Bölümü İçin)
lottie_ai = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_3rwasyjy.json")

# --- Başlık Bölümü ---
# Sol tarafa animasyon, sağ tarafa başlık koyalım
with st.container():
    col_anim, col_title = st.columns([1, 4])
    with col_anim:
        if lottie_sustainability:
            st_lottie(lottie_sustainability, height=120, key="main_anim")
    with col_title:
        st.title("GreenBudget AI: Sürdürülebilir Mali Asistan")
        st.markdown("""
        Kamu Maliyesi disiplini ile yapay zekayı birleştirerek harcamalarınızın 
        **Karbon Ayak İzini** ve potansiyel **Yeşil Vergi** yükünü hesaplarız.
        """)

st.divider()

# --- Kullanıcı Girişleri (Sidebar) ---
st.sidebar.markdown("## :moneybag: Aylık Harcama Verileri")
ulasim = st.sidebar.number_input("Akaryakıt Harcaması (TL)", min_value=0, help="Benzin veya Motorin harcamalarınız.")
elektrik = st.sidebar.number_input("Elektrik Faturası (TL)", min_value=0)
dogalgaz = st.sidebar.number_input("Doğalgaz Faturası (TL)", min_value=0)
su = st.sidebar.number_input("Su Faturası (TL)", min_value=0)
gida = st.sidebar.number_input("Gıda Harcaması (TL)", min_value=0, help="Market ve restoran harcamalarınız.")

# --- Güncellenmiş Katsayılar ---
CO2_ULASIM = 0.0005 
CO2_ELEKTRIK = 0.0004
CO2_DOGALGAZ = 0.0003
CO2_SU = 0.0001
CO2_GIDA = 0.0001
KARBON_VERGI_ORANI = 0.15

# --- Hesaplamalar ---
toplam_co2 = (ulasim * CO2_ULASIM) + (elektrik * CO2_ELEKTRIK) + \
             (dogalgaz * CO2_DOGALGAZ) + (su * CO2_SU) + (gida * CO2_GIDA)

potansiyel_vergi = toplam_co2 * KARBON_VERGI_ORANI

# --- Sonuç Ekranı ---
col_co2, col_tax = st.columns(2)
with col_co2:
    st.subheader(":factory: Tahmini Toplam Karbon")
    st.metric(label="", value=f"{toplam_co2:.2f} kg CO2", help="Toplam karbon ayak iziniz.")
with col_tax:
    st.subheader(":classical_building: Simüle Edilen Yeşil Vergi")
    st.metric(label="", value=f"{potansiyel_vergi:.2f} TL", help="%15 oranında simüle edilmiş vergi yükü.")

st.divider()

# --- Görselleştirme Katmanı ---
if toplam_co2 > 0:
    st.subheader(":chart_with_upwards_trend: Karbon Kaynaklarınızın Dağılımı")
    
    tum_kategoriler = ['Ulaşım', 'Elektrik', 'Doğalgaz', 'Su', 'Gıda']
    tum_emisyonlar = [ulasim * CO2_ULASIM, elektrik * CO2_ELEKTRIK, dogalgaz * CO2_DOGALGAZ, su * CO2_SU, gida * CO2_GIDA]
    tum_renkler = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

    aktif_veriler, aktif_etiketler, aktif_renkler = [], [], []
    for idx, emisyon in enumerate(tum_emisyonlar):
        if emisyon > 0:
            aktif_veriler.append(emisyon)
            aktif_etiketler.append(tum_kategoriler[idx])
            aktif_renkler.append(tum_renkler[idx])
    
    if aktif_veriler:
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.pie(aktif_veriler, labels=aktif_etiketler, autopct='%1.1f%%', 
                startangle=90, colors=aktif_renkler, 
                labeldistance=1.1, pctdistance=0.8)
        
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig1.gca().add_artist(centre_circle)
        st.pyplot(fig1)

# --- AI Tavsiyesi ---
with st.container():
    col_ai_anim, col_ai_text = st.columns([1, 4])
    with col_ai_anim:
        if lottie_ai:
            st_lottie(lottie_ai, height=100, key="ai_anim")
    with col_ai_text:
        st.subheader("🤖 AI Sürdürülebilirlik Tavsiyesi")
        if toplam_co2 > 15:
            st.warning("Karbon ayak iziniz yüksek! Enerji tasarrufu ve toplu taşıma kullanımı hem bütçenizi hem de doğayı korur.")
        elif toplam_co2 > 0:
            st.success("Harika! Sürdürülebilir bir tüketim dengesi kurmuşsunuz.")
        else:
            st.info("Lütfen hesaplama yapmak için verilerinizi giriniz.")

st.divider()
st.info("Bu proje Future Talent Program 201 Bitirme Projesi olarak geliştirilmiştir.")
