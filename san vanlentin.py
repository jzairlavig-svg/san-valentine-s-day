import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi niña linda", page_icon="❤️")

# Estilos personalizados con CSS
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
    .stButton>button:hover {
        background-color: #ff758f;
        color: white;
        border: 1px solid #ff4b6b;
    }
    h1 {
        color: #c9184a !important;
        text-align: center;
    }
    p {
        text-align: center;
        font-size: 20px;
        color: #590d22;
    }
    div[data-testid="stImage"] > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Una pregunta muy importante...")

st.write("Hola Lubaloo, he estado pensando mucho en esto y quería decírtelo de una forma especial...")

# He cambiado el enlace por uno más estable de GIPHY
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3bmZqZzR4eXh4eXh4eXh4eXh4eXh4eXh4eXh4eXh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/K67869X0z7SOf2R809/giphy.gif")

st.markdown("<h3 style='text-align: center; color: #c9184a;'>¿Quieres ser mi San Valentín?</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ! 😍"):
        st.balloons()
        st.success("¡Sabía que dirías que sí! Te quiero muchísimo. ❤️")
        # Se eliminó st.confetti() para evitar el AttributeError

with col2:
    if st.button("No... 😢"):
        respuestas_no = [
            "¿Estás segura? Piénsalo bien...",
            "Esa opción está dañada, intenta con la de al lado.",
            "¡Error 404: Respuesta no encontrada!",
            "Inténtalo de nuevo, creo que te equivocaste de botón.",
            "Mi corazón no puede procesar un 'No'"
        ]
        st.warning(random.choice(respuestas_no))

# Pie de página
st.markdown("---")
st.markdown("<p style='font-size: 14px; color: #800f2f;'>Hecho con ❤️ por Justin</p>", unsafe_allow_html=True)
