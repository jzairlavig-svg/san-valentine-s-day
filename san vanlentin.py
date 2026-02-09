import streamlit as st
from datetime import datetime, timedelta
import random

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹", layout="centered")

# --- 2. ESTILOS CSS (Diseño Completo y Colorido) ---
st.markdown("""
    <style>
    /* FONDO DE CORAZONES */
    .stApp {
        background-color: #ffdde1;
        background-image: url("data:image/svg+xml,%3Csvg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M32 56C14.327 40 4 28 4 16 4 9.373 9.373 4 16 4c4.18 0 7.843 2.14 10 5.36C28.157 6.14 31.82 4 36 4c6.627 0 12 5.373 12 12 0 12-10.327 24-28 40z' fill='%23eebbc3' fill-opacity='0.6' fill-rule='evenodd'/%3E%3C/svg%3E");
        background-attachment: fixed;
    }

    /* ANIMACIÓN DE CAÍDA (LLUVIA) */
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

    /* ESTILO PARA LAS CAJAS DE "3 RAZONES" (EXPANDERS) */
    .streamlit-expanderHeader {
        background-color: #ffe5ec; /* Fondo rosado suave */
        color: #d61c4e; /* Texto rojo oscuro */
        font-weight: bold;
        border-radius: 10px;
        border: 1px solid #ffcad4;
    }
    .streamlit-expanderContent {
        background-color: white;
        border-radius: 0 0 10px 10px;
        border: 1px solid #ffcad4;
        border-top: none;
        color: #5d0e24;
    }
    
    /* MENSAJES DE RESPUESTA (SÍ/NO) PERSONALIZADOS */
    .mensaje-exito {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #c3e6cb;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        margin-top: 20px;
    }
    .mensaje-error {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #f5c6cb;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        margin-top: 20px;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.8);
        border-right: 2px solid #ffcad4;
    }

    /* TIMER */
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 5px;
        border: 1px solid #ff2e63;
        text-align: center;
    }
    div[data-testid="stMetricLabel"] { font-size: 14px !important; color: #d61c4e !important; font-weight: bold; }
    div[data-testid="stMetricValue"] { font-size: 24px !important; color: #ff2e63 !important; }

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
    }
    .stButton>button:hover { background-color: #ff0040; transform: scale(1.03); }
    
    /* TEXTOS */
    h1 { color: #d61c4e !important; text-shadow: 2px 2px 0px white; font-family: serif; text-align: center; }
    h3 { color: #ff2e63 !important; text-align: center; font-family: sans-serif; font-size: 20px; margin-top: 20px;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LLUVIA DE CORAZONES ---
def lluvia_corazones():
    html_corazones = ""
    for _ in range(15):
        left = random.randint(0, 100)
        delay = random.random() * 5
        duration = random.randint(5, 10)
        size = random.randint(10, 30)
        html_corazones += f"<div class='corazon-flotante' style='left: {left}%; animation-delay: {delay}s; animation-duration: {duration}s; font-size: {size}px;'>❤️</div>"
    st.markdown(html_corazones, unsafe_allow_html=True)

lluvia_corazones()

# --- 4. BARRA LATERAL (Arreglada) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #d61c4e;'>Nuestra Historia ❤️</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("**💑 Protagonistas:** Justin & Lubaloo")
    st.write("**🗓️ Tiempo Juntos:** 10 Meses")
    st.write("**🎶 Nuestra Canción:** Winter Bear")
    st.write("**📍 Próxima parada:** San Valentín")
    st.markdown("---")
    # Imagen de ositos estable (de Unsplash) para que no falle
    st.image("https://images.unsplash.com/photo-1585155967849-91c73653ace3?q=80&w=600&auto=format&fit=crop", caption="Love You", use_container_width=True)

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

st.markdown("<h3 style='margin-bottom: 10px;'>⏳ Countdown to Valentine's</h3>", unsafe_allow_html=True)

if es_hoy:
    st.balloons()
    st.success("¡FELIZ SAN VALENTÍN! ❤️🌹✨")
else:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Días", dias)
    c2.metric("Horas", horas)
    c3.metric("Mins", minutos)
    c4.metric("Segs", segundos)

# --- 6. LA CARTA ---
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

# --- 7. RAZONES (Con Cajas de Colores) ---
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
    st.image("foto.jpg", caption="Tú y Yo ❤️", use_container_width=True)
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
        # MENSAJE DE ÉXITO PERSONALIZADO (ROJO/ROSADO)
        st.markdown("""
            <div style="background-color: #ffe5ec; color: #d61c4e; padding: 20px; border-radius: 15px; border: 2px solid #ff4b6b; text-align: center; margin-top: 15px;">
                <h3 style="color: #ff2e63; margin:0;">¡SABÍA QUE DIRÍAS QUE SÍ! ❤️</h3>
                <p style="font-size: 18px; font-weight: bold; margin-top: 10px;">
                    ¡Me haces el hombre más feliz del mundo, mi pequeña Lubaloo! <br>
                    Prometo que tendremos un San Valentín inolvidable. ¡Te amo! 💑
                </p>
            </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("No... 😢"):
        # MENSAJE DE ERROR PERSONALIZADO
        st.markdown("""
            <div style="background-color: #f8d7da; color: #721c24; padding: 15px; border-radius: 15px; border: 2px solid #f5c6cb; text-align: center; margin-top: 15px;">
                <p style="font-size: 18px; font-weight: bold;">
                    🚫 ¡Opción Bloqueada por Cupido! <br> 
                    Intenta darle al botón de la izquierda. 😉
                </p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #880d1e;'>Para: Lubaloo | De: Justin — Febrero 2026</div>", unsafe_allow_html=True)
