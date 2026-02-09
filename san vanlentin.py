import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹")

# Estilos personalizados: Diseño con degradado y efectos visuales
st.markdown("""
    <style>
    /* Fondo con degradado romántico */
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    
    /* Contenedor de la carta tipo pergamino moderno */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 50px;
        border-radius: 30px;
        border: 3px solid #ffffff;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.1);
        color: #5d0e24;
        margin-bottom: 30px;
        text-align: justify;
        backdrop-filter: blur(5px);
    }

    .titulo-principal {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        text-align: center;
        font-family: 'serif';
        font-size: 40px;
        margin-bottom: 20px;
    }

    /* Estilo para los botones */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 4em;
        background-color: #ff4b6b;
        color: white;
        border: none;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0px 8px 15px rgba(255, 75, 107, 0.4);
        transition: all 0.3s ease 0s;
    }

    .stButton>button:hover {
        background-color: #ff758f;
        transform: translateY(-5px);
        box-shadow: 0px 15px 20px rgba(255, 117, 143, 0.4);
    }

    .firma {
        text-align: right;
        font-family: 'cursive';
        font-size: 24px;
        color: #c9184a;
        margin-top: 30px;
    }

    /* Imagen con bordes artísticos */
    div[data-testid="stImage"] > img {
        display: block;
        margin: 0 auto;
        border-radius: 30px;
        border: 5px solid white;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='titulo-principal'>❤️ Una propuesta desde el corazón</h1>", unsafe_allow_html=True)

# Carta con tu texto personalizado
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 22px; font-weight: bold; color: #c9184a;">Mi adorada Lubaloo,</p>
        <p style="font-size: 19px; line-height: 1.9;">
            Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. 
            En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br>
            A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. 
            Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. 
            Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br>
            Se acerca <b>San Valentín</b>, un día que celebra lo que nosotros vivimos a diario. Por eso, no quería que fuera una fecha cualquiera. 
            Quiero que sea un momento para recordarte cuánto te amo y lo mucho que deseo seguir caminando de tu mano.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 26px; color: #ff4b6b; margin-top: 30px; font-family: 'serif';">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
        <p class="firma">Con todo mi amor, Justin</p>
    </div>
    """, unsafe_allow_html=True)

# CARGA DE LA FOTO (Recuerda que debe llamarse foto.jpg en GitHub)
try:
    st.image("foto.jpg", use_container_width=True)
except:
    st.info("Cargando nuestra foto especial... ❤️")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.snow()
        st.success("¡Me haces el hombre más feliz del mundo! Prometo que será un San Valentín inolvidable. ¡Te amo demasiado! ❤️")

with col2:
    if st.button("No... 😢"):
        frases = [
            "¿Estás segura? Ese botón rosa de al lado se ve mucho mejor... ✨",
            "¡Error! Este botón ha sido desactivado por exceso de amor. 😊",
            "Piénsalo bien, Lubaloo... ¡habrá muchas sorpresas! 🍫",
            "Mi corazón dice que querías presionar el botón de la izquierda. 🌹",
            "¡Inténtalo de nuevo! El amor siempre da segundas oportunidades. ❤️"
        ]
        st.warning(random.choice(frases))

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: white; font-size: 16px; font-weight: bold;'>Para: Lubaloo | De: Justin — Febrero 2026</p>", unsafe_allow_html=True)
