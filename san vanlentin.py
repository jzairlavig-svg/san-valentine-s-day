import streamlit as st
import random

# --- CONFIGURACIÓN DE PÁGINA (Debe ser lo primero) ---
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹")

# --- ESTILOS CSS (Fondo de Corazones y Diseño Cristal) ---
st.markdown("""
    <style>
    /* Imagen de fondo romántica */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1612452830763-568fb16926bb?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Caja de la carta con efecto vidrio */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid white;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
        color: #5d0e24;
        margin-bottom: 20px;
        text-align: justify;
    }
    
    /* Título estilizado */
    .titulo-nuevo {
        color: #c9184a !important;
        text-shadow: 2px 2px 0px #ffffff;
        text-align: center;
        font-family: serif;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 15px;
    }

    /* Botones bonitos */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 50px;
        background-color: #ff4b6b;
        color: white;
        font-weight: bold;
        border: 2px solid white;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.2);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        background-color: #d6284a;
    }

    .firma {
        text-align: right;
        font-style: italic;
        font-weight: bold;
        color: #c9184a;
        margin-top: 15px;
    }
    
    .musica-texto {
        text-align: center;
        color: white;
        font-weight: bold;
        background-color: #ff4b6b;
        padding: 5px;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* Ajuste del video para que parezca audio */
    div.stVideo {
        margin: 0 auto;
        width: 100%;
        max-width: 400px; /* Limita el ancho del reproductor */
    }
    iframe {
        height: 200px;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.markdown("<h1 class='titulo-nuevo'>🌹 Una pregunta desde mi corazón 🌹</h1>", unsafe_allow_html=True)

# Carta
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 20px; font-weight: bold; color: #c9184a;">Mi adorada Lubaloo,</p>
        <p style="font-size: 18px; line-height: 1.6;">
            Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. 
            En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br>
            A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. 
            Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. 
            Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br>
            Se acerca <b>San Valentín</b>, un día que celebra lo que nosotros vivimos a diario. Por eso, no quería que fuera una fecha cualquiera. 
            Quiero que sea un momento para recordarte cuánto te amo y lo mucho que deseo seguir caminando de tu mano.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 24px; color: #ff4b6b; margin-top: 20px;">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
        <p class="firma">Con todo mi amor, Justin</p>
    </div>
    """, unsafe_allow_html=True)

# Música
col_musica1, col_musica2, col_musica3 = st.columns([1, 2, 1])
with col_musica2:
    st.markdown("<div style='text-align: center;'><p class='musica-texto'>🎵 Dale play a nuestra canción...</p></div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=1iK-ttRjV-E")

st.markdown("<br>", unsafe_allow_html=True)

# Foto (Con manejo de errores seguro)
try:
    # Usamos use_column_width que es compatible con versiones viejas y nuevas
    st.image("foto.jpg", use_column_width=True) 
except:
    st.warning("⚠️ No se pudo cargar la foto. Asegúrate de que el archivo en GitHub se llame 'foto.jpg' (minúsculas).")

st.markdown("<br>", unsafe_allow_html=True)

# Botones
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
st.markdown("<p style='text-align: center; color: white; background-color: rgba(0,0,0,0.3); padding: 5px; border-radius: 10px;'>Para: Lubaloo | De: Justin — Febrero 2026</p>", unsafe_allow_html=True)
