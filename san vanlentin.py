import streamlit as st
import random
import os

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹")

# Estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 30px;
        border-left: 10px solid #ff4b6b;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.1);
        color: #5d0e24;
        margin-bottom: 25px;
        text-align: justify;
        backdrop-filter: blur(10px);
    }
    .titulo-nuevo {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
        font-family: 'serif';
        font-size: 35px;
        font-weight: bold;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 4em;
        background-color: #ff4b6b;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
    }
    .firma {
        text-align: right;
        font-style: italic;
        font-weight: bold;
        color: #c9184a;
        margin-top: 25px;
        font-size: 20px;
    }
    .musica-texto {
        text-align: center;
        color: #5d0e24;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='titulo-nuevo'>🌹 Una pregunta desde mi corazón 🌹</h1>", unsafe_allow_html=True)

# Carta con tu mensaje personalizado
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 22px; font-weight: bold; color: #c9184a;">Mi adorada Lubaloo,</p>
        <p style="font-size: 19px; line-height: 1.8;">
            Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. 
            En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br>
            A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. 
            Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. 
            Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br>
            Se acerca <b>San Valentín</b>, un día que celebra lo que nosotros vivimos a diario. Por eso, no quería que fuera una fecha cualquiera. 
            Quiero que sea un momento para recordarte cuánto te amo y lo mucho que deseo seguir caminando de tu mano.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 26px; color: #ff4b6b; margin-top: 30px;">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
        <p class="firma">Con todo mi amor, Justin</p>
    </div>
    """, unsafe_allow_html=True)

# SECCIÓN DE AUDIO (Usando el archivo local musica.mp3)
st.markdown("<p class='musica-texto'>🎵 Dale play para escuchar Winter Bear mientras lees...</p>", unsafe_allow_html=True)

if os.path.exists("musica.mp3"):
    with open("musica.mp3", "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3")
else:
    st.write("Subiendo la música... ❤️")

# Imagen
try:
    st.image("foto.jpg", use_container_width=True)
except:
    st.info("Cargando nuestra foto... ❤️")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.snow()
        st.success("¡Me haces el hombre más feliz del mundo! ¡Te amo demasiado! ❤️")

with col2:
    if st.button("No... 😢"):
        st.warning("Esa opción no existe hoy, intenta el botón de al lado. 😊")

st.markdown("---")
st.markdown("<p style='text-align: center; color: white; font-weight: bold;'>Para: Lubaloo | De: Justin — Febrero 2026</p>", unsafe_allow_html=True)
