import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

# ── Sayfa ayarları ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="Oyun Bağımlılığı Analizi",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Dengeli ve Kompakt CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
    }

    .stApp { background: #f8fafc; }
    
    .header-compact {
        background: #0f172a;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 1.5rem;
        color: white;
    }
    
    .card-small {
        background: white;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }

    .risk-box {
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 1rem;
    }
    .low      { background: #10b981; }
    .moderate { background: #f59e0b; }
    .high     { background: #ef4444; }
    .severe   { background: #8b5cf6; }

    .report-section {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
    }
    
    .report-item {
        display: flex;
        margin-bottom: 0.8rem;
        font-size: 0.9rem;
    }

    .stButton>button {
        background: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ── Model yükleme ────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    base = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(base, 'model_files')
    try:
        with open(os.path.join(model_dir, 'model.pkl'), 'rb') as f:
            model = pickle.load(f)
        with open(os.path.join(model_dir, 'scaler.pkl'), 'rb') as f:
            scaler = pickle.load(f)
        with open(os.path.join(model_dir, 'label_encoders.pkl'), 'rb') as f:
            label_encoders = pickle.load(f)
        with open(os.path.join(model_dir, 'X_columns.pkl'), 'rb') as f:
            X_columns = list(pickle.load(f))
        return model, scaler, label_encoders, X_columns, True
    except:
        return None, None, None, None, False

model, scaler, label_encoders, X_columns, model_loaded = load_model()

def guvenli_encode(sutun_adi, secilen_deger):
    if sutun_adi in label_encoders:
        try: return label_encoders[sutun_adi].transform([str(secilen_deger)])[0]
        except: return 0
    return 0

# ── HEADER ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-compact">
    <h2 style="color:white; margin:0;">🎮 Oyun Bağımlılığı Risk Analizi</h2>
    <p style="color:#94a3b8; margin:0; font-size:0.9rem;">Emre AYVAZ · 24100011085 · Necmettin Erbakan Üniversitesi</p>
</div>
""", unsafe_allow_html=True)

if not model_loaded:
    st.error("⚠️ Model dosyaları eksik!")
    st.stop()

# ── FORM (TÜM SORULAR) ───────────────────────────────────────────────────
with st.form("main_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("####  Demografik Bilgiler")
        age = st.slider("Yaş", 13, 40, 20)
        gender = st.selectbox("Cinsiyet", ["Male", "Female", "Other"], format_func=lambda x: "Erkek" if x=="Male" else ("Kadın" if x=="Female" else "Diğer"))
        years_gaming = st.slider("Oyun Geçmişi (Yıl)", 1, 20, 5)
        monthly_spend = st.number_input("Aylık Harcama ($)", value=50)
        daily_hours = st.slider("Günlük Oyun (Saat)", 0.5, 16.0, 4.0)
        platform = st.selectbox("Platform", ['PC', 'Multi-platform', 'Console', 'Mobile'])

    with col2:
        st.markdown("#### 🕹️ Oyun Alışkanlıkları")
        genre = st.selectbox("Oyun Türü", ['Mobile Games', 'MOBA', 'FPS', 'RPG', 'Battle Royale', 'MMO', 'Strategy'])
        primary = st.selectbox("Ana Oyun", ['CS:GO', 'League of Legends', 'Valorant', 'PUBG', 'Fortnite', 'Dota 2', 'GTA V'])
        mood_swing = st.selectbox("Duygu Değişim Sıklığı", ['Never', 'Rarely', 'Sometimes', 'Often', 'Daily'])
        mood_state = st.selectbox("Genel Ruh Hali", ['Normal', 'Anxious', 'Irritable', 'Depressed', 'Angry', 'Excited'])
        sleep_h = st.slider("Uyku (Saat)", 3.0, 10.0, 7.0)
        sleep_q = st.selectbox("Uyku Kalitesi", ['Good', 'Fair', 'Poor', 'Very Poor', 'Insomnia'])

    with col3:
        st.markdown("####  Sağlık ve Sosyal")
        performance = st.selectbox("Başarı/Verimlilik", ['Excellent', 'Good', 'Average', 'Below Average', 'Poor', 'Failing'])
        social_iso = st.slider("Yalnızlık Skoru", 1, 10, 3)
        face_social = st.slider("Yüz Yüze Sosyal (Saat/Hafta)", 0, 20, 7)
        weight_kg = st.slider("Kilo Değişimi (kg)", 0, 15, 1)
        exercise_h = st.slider("Egzersiz (Saat/Hafta)", 0, 15, 3)
        
        st.markdown("#### ⚠️ Semptomlar")
        loss_int = st.checkbox("İlgi Kaybı")
        cont_prob = st.checkbox("Sorunlara Rağmen Devam")
        eye_str = st.checkbox("Göz Yorgunluğu")
        pain = st.checkbox("Sırt/Boyun Ağrısı")

    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.form_submit_button("RİSKİ HESAPLA")

# ── TAHMİN VE RAPOR ──────────────────────────────────────────────────────
if predict_btn:
    # Logic
    intensity = daily_hours / (age + 1)
    input_data = {
        'age': age, 'gender': guvenli_encode('gender', gender), 'daily_gaming_hours': daily_hours,
        'game_genre': guvenli_encode('game_genre', genre), 'primary_game': guvenli_encode('primary_game', primary),
        'gaming_platform': guvenli_encode('gaming_platform', platform), 'sleep_hours': sleep_h,
        'sleep_quality': guvenli_encode('sleep_quality', sleep_q), 
        'sleep_disruption_frequency': 0, 'academic_work_performance': guvenli_encode('academic_work_performance', performance), 
        'grades_gpa': 2.5, 'work_productivity_score': 5,
        'mood_state': guvenli_encode('mood_state', mood_state), 'mood_swing_frequency': guvenli_encode('mood_swing_frequency', mood_swing),
        'loss_of_other_interests': int(loss_int), 'continued_despite_problems': int(cont_prob),
        'weight_change_kg': weight_kg, 'exercise_hours_weekly': exercise_h, 'social_isolation_score': social_iso,
        'face_to_face_social_hours_weekly': face_social, 'monthly_game_spending_usd': monthly_spend,
        'years_gaming': years_gaming, 'gaming_intensity': intensity,
        'eye_strain': int(eye_str), 'back_neck_pain': int(pain)
    }
    
    input_df = pd.DataFrame([input_data]).reindex(columns=X_columns, fill_value=0)
    input_scaled = scaler.transform(input_df)
    
    prediction = model.predict(input_scaled)[0]
    probs = model.predict_proba(input_scaled)[0]
    prob_dict = {str(cls): float(p) for cls, p in zip(model.classes_, probs)}

    st.markdown("---")
    res_col1, res_col2 = st.columns([1, 1.2])

    with res_col1:
        cfg = {
            'Low': ('🟢', 'DÜŞÜK RİSK', 'low', 'Dengeli alışkanlıklar.'),
            'Moderate': ('🟡', 'ORTA RİSK', 'moderate', 'Dikkat edilmesi önerilir.'),
            'High': ('🟠', 'YÜKSEK RİSK', 'high', 'Yaşam kalitesi etkileniyor.'),
            'Severe': ('🔴', 'KRİTİK RİSK', 'severe', 'Profesyonel destek önerilir.')
        }
        emoji, label, css, sub = cfg.get(prediction, cfg['Moderate'])
        
        st.markdown(f"""
        <div class="risk-box {css}">
            <div style="font-size:2.5rem;">{emoji}</div>
            <h2 style="color:white; margin:0;">{label}</h2>
            <p style="margin:0;">{sub}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Olasılık Dağılımı**")
        for k, v in {'Low':'Düşük', 'Moderate':'Orta', 'High':'Yüksek', 'Severe':'Kritik'}.items():
            st.progress(prob_dict.get(k, 0.0), text=f"{v}: %{prob_dict.get(k, 0.0)*100:.1f}")

    with res_col2:
        st.markdown("""<div class="report-section">
            <h4 style="margin-top:0;"> Analiz Raporu</h4>""", unsafe_allow_html=True)
        
        st.markdown(f" **Genel Durum:** Modelimiz verilerinizi analiz etti ve risk seviyenizi **{label}** olarak belirledi.")
        st.markdown(f" **Kritik Veri:** Günlük **{daily_hours} saat** oyun süresi, yaşınıza göre yoğun bir kullanım olarak saptanmıştır.")
        st.markdown(f" **Sosyal Etki:** Haftalık **{face_social} saat** yüz yüze etkileşim, risk puanınızı dengeleyen/artıran bir faktördür.")
        st.markdown(f"💡 **Öneri:** {sub} Uyku kalitenizi artırmak için yatmadan 1 saat önce ekran kullanımını kısıtlamanız önerilir.")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<center><small>© 2026 Emre AYVAZ</small></center>", unsafe_allow_html=True)