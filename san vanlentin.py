import streamlit as st
from datetime import datetime, timedelta
import random
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹", layout="centered")

# --- 2. ESTILOS CSS (ESTILOS COMPLETOS) ---
st.markdown("""
    <style>
    /* FONDO DE CORAZONES ESTÁTICO */
    .stApp {
        background-color: #ffdde1;
        background-image: url("data:image/svg+xml,%3Csvg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M32 56C14.327 40 4 28 4 16 4 9.373 9.373 4 16 4c4.18 0 7.843 2.14 10 5.36C28.157 6.14 31.82 4 36 4c6.627 0 12 5.373 12 12 0 12-10.327 24-28 40z' fill='%23eebbc3' fill-opacity='0.6' fill-rule='evenodd'/%3E%3C/svg%3E");
        background-attachment: fixed;
    }

    /* ANIMACIÓN DE CAÍDA (LLUVIA DE CORAZONES) */
    @keyframes falling {
        0% { transform: translateY(-10vh); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }
    .corazon-flotante {
        position: fixed;
        color: #ff4b6b;
        font-size: 20px;
        animation: falling 8s linear infinite;
        z-index: 0;
    }

    /* CARTA PRINCIPAL */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ffcad4;
        box-shadow: 0px 8px 20px rgba(214, 28, 78, 0.15);
        color: #880d1e;
        margin-bottom: 20px;
        text-align: justify;
        position: relative;
        z-index: 1;
    }

    /* --- ESTILOS DE CAJAS (EXPANDERS) --- */
    .streamlit-expanderHeader {
        background-color: #ffe5ec !important;
        color: #d61c4e !important;
        border: 2px solid #ffcad4 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    .streamlit-expanderContent {
        background-color: #fff0f3 !important;
        border: 1px solid #ffcad4 !important;
        border-top: none !important;
        border-radius: 0 0 10px 10px !important;
        color: #880d1e !important;
    }
    
    /* Compatibilidad navegadores */
    details { background-color: #ffe5ec; border-radius: 10px; margin-bottom: 10px; border: 2px solid #ffcad4; }
    summary { background-color: #ffe5ec; color: #d61c4e; font-weight: bold; padding: 10px; border-radius: 10px; }
    
    /* SIDEBAR ESTILIZADO */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.9);
        border-right: 3px solid #ffcad4;
    }

    /* CAJITAS DE DATOS EN SIDEBAR */
    .dato-box {
        background-color: #fff0f3;
        padding: 10px;
        border-radius: 10px;
        border-left: 5px solid #ff4b6b;
        margin-bottom: 10px;
        font-size: 14px;
        color: #880d1e;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }

    /* TIMER */
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 10px;
        border: 2px solid #ff2e63;
        text-align: center;
        padding: 5px;
        position: relative; z-index: 1;
    }
    div[data-testid="stMetricLabel"] { color: #ff2e63 !important; font-weight: bold; }
    div[data-testid="stMetricValue"] { color: #d61c4e !important; }

    /* BOTONES */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 50px;
        background-color: #ff2e63;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        position: relative; z-index: 1;
    }
    .stButton>button:hover { background-color: #ff0040; transform: scale(1.05); }
    
    /* TEXTOS */
    h1 { color: #d61c4e !important; text-shadow: 2px 2px 0px white; font-family: serif; text-align: center; position: relative; z-index: 1; }
    h3 { color: #ff2e63 !important; text-align: center; font-family: sans-serif; font-size: 20px; margin-top: 20px; position: relative; z-index: 1;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LLUVIA DE CORAZONES ---
def lluvia_corazones():
    html_corazones = ""
    for _ in range(20):
        left = random.randint(0, 100)
        delay = random.random() * 5
        duration = random.randint(5, 10)
        size = random.randint(15, 35)
        html_corazones += f"<div class='corazon-flotante' style='left: {left}%; animation-delay: {delay}s; animation-duration: {duration}s; font-size: {size}px;'>❤️</div>"
    st.markdown(html_corazones, unsafe_allow_html=True)

lluvia_corazones()

# --- 4. BARRA LATERAL (¡AHORA MÁS LLENA!) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #d61c4e;'>Nuestra Historia ❤️</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Tarjetas de datos para llenar espacio
    st.markdown("""
    <div class="dato-box">
        <strong>💑 Protagonistas:</strong><br>Justin & Lubaloo
    </div>
    <div class="dato-box">
        <strong>🗓️ Tiempo Juntos:</strong><br>10 Meses llenos de amor
    </div>
    <div class="dato-box">
        <strong>🎶 Nuestra Canción:</strong><br>Winter Bear 🐻❄️
    </div>
    <div class="dato-box">
        <strong>📍 Próxima parada:</strong><br>San Valentín
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("**📈 Nivel de Amor: Camino al Año**")
    st.progress(10/12) # Barra de progreso (10 meses de 12)
    
    st.markdown("---")
    
    # SNOOPY
    if os.path.exists("snoopy.jpg"):
        st.image("snoopy.jpg", width=200)
    elif os.path.exists("snoopy.png"):
        st.image("snoopy.png", width=200)
    else:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/240px-Heart_coraz%C3%B3n.svg.png", width=150)

    # Frase final para llenar el fondo
    st.markdown("""
    <div style="text-align: center; margin-top: 20px; background-color: #ffe5ec; padding: 10px; border-radius: 10px; border: 1px dashed #ff4b6b;">
        <p style="font-size: 14px; font-style: italic; color: #d61c4e; margin: 0;">
            "Contigo cada día es una nueva aventura." <br> 
            <b>Juntos x Siempre</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. ENCABEZADO Y TIMER ---
st.markdown("<h1>🌹 Para mi pequeña Lubaloo 🌹</h1>", unsafe_allow_html=True)

def get_time_left():
    ahora_utc = datetime.utcnow()
    ahora_peru = ahora_utc - timedelta(hours=5)
    target_year = ahora_peru.year
    target = datetime(target_year, 2, 14)
    if ahora_peru > target + timedelta(days=1): target = datetime(target_year + 1, 2, 14)
    restante = target - ahora_peru
    if restante.total_seconds() < 0 and restante.days == -1: return 0, 0, 0, 0, True 
    return restante.days, restante.seconds // 3600, (restante.seconds // 60) % 60, restante.seconds % 60, False

dias, horas, minutos, segundos, es_hoy = get_time_left()

st.markdown("<h3 style='margin-bottom: 10px;'>⏳ Cuenta regresiva oficial</h3>", unsafe_allow_html=True)

if es_hoy:
    st.balloons()
    st.success("¡FELIZ SAN VALENTÍN! ❤️🌹✨")
else:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Días", dias)
    c2.metric("Horas", horas)
    c3.metric("Mins", minutos)
    c4.metric("Segs", segundos)

# --- 6. CARTA ---
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 20px; font-weight: bold; color: #d61c4e;">Mi adorada Lubaloo,</p>
        <p style="font-size: 18px; line-height: 1.6;">
            Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. 
            En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br>
            A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. 
            Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. 
            Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br>
            Se acerca <b>San Valentín</b>, y no quería que fuera una fecha cualquiera. Quiero que sea un recordatorio de cuánto te amo y lo mucho que deseo seguir caminando de tu mano.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. RAZONES ---
st.markdown("<h3>💖 3 Razones por las que te elijo</h3>", unsafe_allow_html=True)
col_a, col_b, col_c = st.columns(3)
with col_a:
    with st.expander("Tu Sonrisa ✨"):
        st.write("Me ilumina los días, incluso los más grises. Es mi refugio favorito.")
with col_b:
    with st.expander("Tu Apoyo 💪"):
        st.write("Gracias por estar ahí en los momentos difíciles y hacerme mejor persona.")
with col_c:
    with st.expander("Nosotros 💑"):
        st.write("Amo la complicidad que tenemos y cómo nos entendemos con solo mirarnos.")

st.write("") 

# --- 8. MÚSICA ESCONDIDA ---
with st.expander("🎵 Música de fondo: Winter Bear (Clic aquí)"):
    st.video("https://www.youtube.com/watch?v=1iK-ttRjV-E")

st.write("")

# --- 9. FOTO ---
try:
    if os.path.exists("foto.jpg"):
        st.image("foto.jpg", caption="Tú y Yo ❤️", use_container_width=True)
    else:
        st.warning("⚠️ No olvides subir 'foto.jpg' a GitHub.")
except:
    st.info("⚠️ Sube tu foto 'foto.jpg' para verla aquí.")

# --- 10. PREGUNTA FINAL ---
st.markdown("""
    <div class="carta-contenedor" style="text-align: center; border-color: #ff2e63; margin-top: 20px;">
        <p style="font-size: 22px; font-weight: bold; color: #ff2e63;">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.snow()
        st.markdown("""
            <div style="background-color: #ffe5ec; color: #d61c4e; padding: 20px; border-radius: 15px; border: 2px solid #ff4b6b; text-align: center; margin-top: 15px;">
                <h3 style="color: #ff2e63; margin:0;">¡SABÍA QUE DIRÍAS QUE SÍ! ❤️</h3>
                <p style="font-size: 18px; font-weight: bold; margin-top: 10px;">
                    ¡Me haces el hombre más feliz del mundo! <br>Te amo Lubaloo 💑
                </p>
            </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("No... 😢"):
        st.markdown("""
            <div style="background-color: #f8d7da; color: #721c24; padding: 15px; border-radius: 15px; border: 2px solid #f5c6cb; text-align: center; margin-top: 15px;">
                <p style="font-size: 18px; font-weight: bold;">
                    🚫 ¡Opción Bloqueada! Mi corazón solo acepta un SÍ. 😉
                </p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #880d1e;'>Para: Lubaloo | De: Justin — Febrero 2026</div>", unsafe_allow_html=True)
