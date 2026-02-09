import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹")

# Estilos personalizados: Fondo de imagen y diseño de cristal
st.markdown("""
    <style>
    /* Imagen de fondo (Cielo rosado) */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Contenedor de la carta con efecto cristal (Glassmorphism) */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.85); /* Blanco semi-transparente */
        padding: 40px;
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        color: #5d0e24;
        margin-bottom: 25px;
        text-align: justify;
        backdrop-filter: blur(5px); /* Efecto borroso detrás de la carta */
    }
    
    .titulo-nuevo {
        color: #5d0e24 !important; /* Color oscuro para que resalte sobre el cielo */
        text-shadow: 2px 2px 4px rgba(255,255,255,0.6);
        text-align: center;
        font-family: 'serif';
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 25px;
        background-color: rgba(255, 255, 255, 0.6);
        padding: 10px;
        border-radius: 20px;
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
        box-shadow: 0px 5px 15px rgba(255, 75, 107, 0.4);
        transition: transform 0.2s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #ff758f;
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
        color: #ffffff;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    /* Reproductor compacto */
    iframe {
        border-radius: 20px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
        height: 200px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='titulo-nuevo'>🌹 Una pregunta desde mi corazón 🌹</h1>", unsafe_allow_html=True)

# Carta con tu mensaje
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

# SECCIÓN DE MÚSICA
st.markdown("<p class='musica-texto'>🎵 Dale play a nuestra canción...</p>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=1iK-ttRjV-E")

# Foto
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
st.markdown("<p style='text-align: center; color: white; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);'>Para: Lubaloo | De: Justin — Febrero 2026</p>", unsafe_allow_html=True)
