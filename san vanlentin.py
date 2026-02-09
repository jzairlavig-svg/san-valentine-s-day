import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="💖")

# Estilos personalizados para un ambiente romántico
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f7;
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
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        color: white;
        transform: scale(1.05);
    }
    h1 {
        color: #c9184a !important;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .carta-amor {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ffb3c1;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
        color: #590d22;
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 25px;
    }
    .destaque {
        color: #c9184a;
        font-weight: bold;
        font-size: 22px;
        text-align: center;
        display: block;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💌 Una carta para ti...")

# Sección sentimental detallada
st.markdown(f"""
    <div class="carta-amor">
        Mi pequeña <b>Lubaloo</b>,<br><br>
        Desde que llegaste a mi vida, cada día ha sido una aventura nueva. No se trata solo de los momentos grandes, 
        sino de las risas compartidas, de cómo me apoyas y de la forma en que haces que todo sea mejor con solo estar presente. <br><br>
        Llevamos <b>10 meses</b> construyendo algo que para mí es lo más valioso que tengo. Me encanta aprender a tu lado, 
        crecer contigo y ver cómo nuestra historia se escribe con cada detalle. Eres mi persona favorita y no imagino 
        celebrar un día como hoy con nadie más que contigo.<br><br>
        Gracias por ser tú, por tu paciencia y por todo el amor que me das.
        <span class="destaque">¡Felices 10 meses, mi amor! 🌹</span>
    </div>
    """, unsafe_allow_html=True)

# Imagen con enlace directo para evitar errores de disponibilidad
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3bmZqZzR4eXh4eXh4eXh4eXh4eXh4eXh4eXh4eXh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/K67869X0z7SOf2R809/giphy.gif")

st.markdown("<h2 style='text-align: center; color: #c9184a; margin-top: 20px;'>¿Aceptarías ser mi San Valentín este año?</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.success("¡Me haces el hombre más feliz del mundo! Te amo demasiado. ❤️")
        st.confetti = True # Solo para lógica visual

with col2:
    # Botón juguetón para el "No"
    if st.button("No... 😢"):
        respuestas_no = [
            "¿Segura? Mira que hay chocolates involucrados... 🍫",
            "Ese botón está roto, intenta con el rosa de al lado. ✨",
            "¡Error del sistema! Tu corazón dice que SÍ. ❤️",
            "Piénsalo bien, mi pequeña Lubaloo... 🌹",
            "No acepto un no por respuesta hoy. 😊"
        ]
        st.warning(random.choice(respuestas_no))

# Pie de página final
st.markdown("---")
st.markdown("<p style='text-align: center; color: #ff4b6b; font-weight: bold;'>Hecho con todo mi corazón por Justin ✨</p>", unsafe_allow_html=True)
