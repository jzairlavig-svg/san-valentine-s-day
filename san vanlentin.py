import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="San Valentín para Lubaloo ❤️", page_icon="🌹")

# Estilos personalizados: Diseño más romántico y limpio
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
        padding: 30px;
        border-radius: 20px;
        border-left: 10px solid #ff4b6b;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        color: #590d22;
        margin-bottom: 20px;
    }
    .titulo-san-valentin {
        color: #c9184a;
        text-align: center;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='titulo-san-valentin'>💖 Una propuesta especial...</h1>", unsafe_allow_html=True)

# Carta con enfoque en San Valentín y sus 10 meses
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 20px;">Mi querida <b>Lubaloo</b>,</p>
        <p style="font-size: 18px; line-height: 1.6;">
            Llegar a estos <b>10 meses</b> a tu lado ha sido el mejor regalo que la vida me ha dado. 
            Contigo he aprendido que el amor está en los detalles, en las risas y en el apoyo incondicional. <br><br>
            Se acerca el 14 de febrero, y no hay nadie en este mundo con quien prefiera compartir 
            la magia de <b>San Valentín</b> que contigo. Eres mi alegría, mi paz y mi persona favorita.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 22px; color: #ff4b6b;">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
    </div>
    """, unsafe_allow_html=True)

# IMAGEN SOLUCIONADA: Usamos un enlace directo a un archivo GIF estático para evitar bloqueos
# Si esta falla, es porque el servidor de Streamlit tiene un firewall; 
# en ese caso, te recomiendo descargar el gif y subirlo a tu GitHub con el nombre "amor.gif"
st.image("https://raw.githubusercontent.com/StevS98/assets/main/love-heart.gif", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ, Mil veces sí! 😍"):
        st.balloons()
        st.success("¡Eres lo mejor que me ha pasado! Prometo que será un San Valentín inolvidable. Te amo. ❤️")

with col2:
    if st.button("No... 😢"):
        frases = [
            "¿Segura? El botón de 'SÍ' brilla más... ✨",
            "Oops, parece que este botón tiene un error, intenta el otro. 😊",
            "¡No se puede decir que no a Justin hoy! 🌹",
            "Piénsalo... habrá muchos mimos y sorpresas. 🍫"
        ]
        st.warning(random.choice(frases))

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #800f2f;'>Con todo mi amor para Lubaloo — Justin 2026</p>", unsafe_allow_html=True)
