import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹")

# Estilos personalizados para una atmósfera romántica
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background-color: #ff4b6b;
        color: white;
        border: none;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0px 4px 10px rgba(255, 75, 107, 0.3);
    }
    .stButton>button:hover {
        background-color: #ff758f;
        color: white;
        transform: translateY(-2px);
    }
    .carta-contenedor {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        border-left: 10px solid #ff4b6b;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        color: #590d22;
        margin-bottom: 25px;
        text-align: justify;
    }
    .titulo-san-valentin {
        color: #c9184a;
        text-align: center;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    .firma {
        text-align: right;
        font-style: italic;
        font-weight: bold;
        color: #c9184a;
        margin-top: 20px;
    }
    div[data-testid="stImage"] > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='titulo-san-valentin'>💖 Una confesión para ti...</h1>", unsafe_allow_html=True)

# Carta con tu texto personalizado st.markdown(f""" <div class="carta-contenedor"> <p style="font-size: 22px; font-weight: bold; color: #c9184a;">Mi adorada Lubaloo,</p> <p style="font-size: 19px; line-height: 1.9;"> Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br> A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br> Se acerca <b>San Valentín</b>, un día que celebra lo que nosotros vivimos a diario. Por eso, no quería que fuera una fecha cualquiera. Quiero que sea un momento para recordarte cuánto te amo y lo mucho que deseo seguir caminando de tu mano. </p> <p style="text-align: center; font-weight: bold; font-size: 26px; color: #ff4b6b; margin-top: 30px; font-family: 'serif';"> ¿Me harías el honor de ser mi San Valentín? 🌹 </p> <p class="firma">Con todo mi amor, Justin</p> </div> """, unsafe_allow_html=True) 

# CARGA DE LA FOTO QUE SUBISTE
try:
    st.image("foto.jpg", use_container_width=True)
except:
    st.write("Cargando nuestra foto especial... ❤️")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.success("¡Me haces el hombre más feliz del mundo! Prometo que será un día inolvidable. ¡Te amo! ❤️")

with col2:
    if st.button("No... 😢"):
        frases = [
            "¿Segura? El botón de al lado tiene más magia... ✨",
            "¡Error! Este botón está temporalmente fuera de servicio por exceso de ternura. 😊",
            "Piénsalo bien... ¡tengo muchas sorpresas planeadas! 🍫",
            "Mi corazón me dice que querías presionar el botón rosa. 🌹"
        ]
        st.warning(random.choice(frases))

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #800f2f; font-size: 14px;'>Para: Lubaloo | De: Justin — Febrero 2026</p>", unsafe_allow_html=True)
