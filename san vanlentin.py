import streamlit as st
import random
from datetime import datetime

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹", layout="centered")

# --- 2. ESTILOS CSS (Fondo de Corazones + Diseño Bonito) ---
st.markdown("""
    <style>
    /* FONDO DE CORAZONES */
    .stApp {
        background-color: #ffdde1;
        background-image: url("data:image/svg+xml,%3Csvg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M32 56C14.327 40 4 28 4 16 4 9.373 9.373 4 16 4c4.18 0 7.843 2.14 10 5.36C28.157 6.14 31.82 4 36 4c6.627 0 12 5.373 12 12 0 12-10.327 24-28 40z' fill='%23eebbc3' fill-opacity='0.6' fill-rule='evenodd'/%3E%3C/svg%3E");
        background-attachment: fixed;
    }
    
    /* CAJAS PRINCIPALES */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #ffcad4;
        box-shadow: 0px 10px 25px rgba(214, 28, 78, 0.15);
        color: #880d1e;
        margin-bottom: 20px;
        text-align: justify;
    }
    
    /* CONTADOR */
    .contador-box {
        background-color: #ff2e63;
        color: white;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 5px 15px rgba(255, 46, 99, 0.3);
    }
    
    /* BOTONES */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 55px;
        background-color: #ff2e63;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff4b6b;
        transform: scale(1.05);
    }
    
    /* TEXTOS */
    h1 { color: #d61c4e !important; text-shadow: 2px 2px 0px white; font-family: serif; text-align: center;}
    h3 { color: #ff2e63 !important; text-align: center; font-family: serif; }
    
    /* FOTOS */
    img { border-radius: 20px; border: 4px solid white; box-shadow: 0px 5px 15px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ENCABEZADO Y CONTADOR ---
st.markdown("<h1>🌹 Para mi pequeña Lubaloo 🌹</h1>", unsafe_allow_html=True)

# Lógica del contador para San Valentín
hoy = datetime.now()
san_valentin = datetime(hoy.year, 2, 14)
if hoy > san_valentin:
    san_valentin = datetime(hoy.year + 1, 2, 14)
falta = san_valentin - hoy
dias = falta.days
horas = falta.seconds // 3600

st.markdown(f"""
    <div class='contador-box'>
        ⏳ Faltan {dias} días y {horas} horas para nuestro San Valentín ✨
    </div>
    """, unsafe_allow_html=True)

# --- 4. LA CARTA ---
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

# --- 5. NUEVA SECCIÓN: RAZONES (Para llenar espacio) ---
st.markdown("<h3>💖 3 Cosas que amo de ti... (Ábrelas)</h3>", unsafe_allow_html=True)

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

st.write("") # Espacio

# --- 6. MÚSICA Y FOTO ---
st.markdown("<h3>🎵 Nuestra canción</h3>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=1iK-ttRjV-E")

st.write("") 

try:
    st.image("foto.jpg", caption="Tú y Yo ❤️", use_container_width=True)
except:
    st.info("⚠️ Sube tu foto 'foto.jpg' para verla aquí.")

# --- 7. LA PREGUNTA FINAL ---
st.markdown("""
    <div class="carta-contenedor" style="text-align: center; border-color: #ff2e63;">
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
        st.success("¡Me haces el hombre más feliz del mundo! ¡Te amo demasiado! ❤️")

with col2:
    if st.button("No... 😢"):
        st.warning("¡Botón equivocado! Mi corazón solo acepta un SÍ. 😊")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #880d1e;'>Para: Lubaloo | De: Justin — Febrero 2026</div>", unsafe_allow_html=True)
