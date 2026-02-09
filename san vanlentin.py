import streamlit as st
import random
from datetime import date

# Configuración de la página
st.set_page_config(page_title="Para Lubaloo ❤️", page_icon="💖")

# Estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b6b;
        color: white;
        border: none;
        font-weight: bold;
    }
    h1 {
        color: #c9184a !important;
        text-align: center;
    }
    .texto-amor {
        text-align: center;
        font-size: 22px;
        color: #590d22;
        font-weight: bold;
    }
    .contador {
        text-align: center;
        font-size: 18px;
        color: #ff4b6b;
        background: white;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Una pregunta muy importante...")

# Sección de aniversario (10 meses)
st.markdown("<p class='texto-amor'>¡Felices 10 meses, mi pequeña Lubaloo! 🌹</p>", unsafe_allow_html=True)
st.markdown("<div class='contador'>Llevamos 10 meses creando una historia increíble juntos.</div>", unsafe_allow_html=True)

# IMAGEN CORREGIDA: Usando una URL de Imgur que es más estable para evitar el error de disponibilidad
st.image("https://i.imgur.com/vH9ZJsh.gif")

st.markdown("<h3 style='text-align: center; color: #c9184a;'>¿Quieres ser mi San Valentín?</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ! 😍"):
        st.balloons()
        st.success("¡Sabía que dirías que sí! Te amo muchísimo, Justin. ❤️")

with col2:
    if st.button("No... 😢"):
        respuestas_no = [
            "¿Estás segura? Piénsalo otra vez...",
            "Esa opción no funciona hoy, intenta la otra.",
            "¡Error! Este botón está de vacaciones.",
            "Inténtalo de nuevo, creo que te equivocaste."
        ]
        st.warning(random.choice(respuestas_no))

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #800f2f;'>Hecho con amor por Justin para Lubaloo ✨</p>", unsafe_allow_html=True)
