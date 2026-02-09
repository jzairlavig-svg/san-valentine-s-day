import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi niña linda", page_icon="❤️")

# Estilos personalizados con CSS
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b6b;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff758f;
        color: white;
    }
    h1 {
        color: #c9184a;
        text-align: center;
    }
    p {
        text-align: center;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Una pregunta muy importante...")

st.write("Hola Lubaloo, he estado pensando mucho en esto y quería decírtelo de una forma especial...")

# Imagen o GIF romántico
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3bmZqZzR4eXh4eXh4eXh4eXh4eXh4eXh4eXh4eXh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/kU765yWn5oB6eQ40Xv/giphy.gif")

st.markdown("### ¿Quieres ser mi San Valentín?")

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ! 😍"):
        st.balloons()
        st.success("¡Sabía que dirías que sí! Te quiero muchísimo. ❤️")
        st.confetti() # Nota: requiere st.snow() o componentes extra, usamos balloons por defecto

with col2:
    # Un pequeño truco: si intenta darle a "No", el botón se mueve o muestra un mensaje gracioso
    if st.button("No... 😢"):
        respuestas_no = [
            "¿Estás segura? Piénsalo bien...",
            "Esa opción está dañada, intenta con la de al lado.",
            "¡Error 404: Respuesta no encontrada!",
            "Inténtalo de nuevo, creo que te equivocaste de botón."
        ]
        st.warning(random.choice(respuestas_no))

# Pie de página
st.markdown("---")
st.markdown("<p style='font-size: 12px;'>Hecho con ❤️ por Justin</p>", unsafe_allow_html=True)
