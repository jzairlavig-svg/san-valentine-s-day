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
        font-size: 45px;
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

st.markdown("<h1 class='titulo-principal'>❤️ Lo que mi corazón dicta...</h1>", unsafe_allow_html=True)

# Carta extendida con sentimientos profundos
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 22px; font-weight: bold; color: #c9184a;">Mi amada Lubaloo,</p>
        <p style="font-size: 19px; line-height: 1.9;">
            A veces me detengo a intentar explicar cómo en tan solo <b>10 meses</b> lograste cambiar mi mundo por completo. 
            Llegaste sin avisar y te convertiste en la respuesta a todas esas preguntas que ni siquiera sabía que tenía. 
            Contigo, cada día es una oportunidad nueva para descubrir que la felicidad no es un destino, sino cada momento 
            que paso escuchando tu risa o simplemente sintiendo tu presencia a mi lado. <br><br>
            Gracias por ser esa persona que me conoce mejor que nadie, por tu paciencia infinita y por la forma en que 
            haces que hasta los días más grises brillen con tu luz. Eres mi refugio seguro y mi aventura favorita. 
            Lo que hemos construido juntos es mi tesoro más grande, y cada pequeño recuerdo es una página de la historia 
            que quiero seguir escribiendo por el resto de mi vida. <br><br>
            Se acerca <b>San Valentín</b>, y aunque sé que el amor se celebra a diario, hoy quiero pedirte formalmente 
            que seas mi compañera en esta fecha tan especial. No porque necesite un día para amarte, sino porque quiero 
            aprovechar cada excusa del calendario para decirte que eres lo más hermoso que me ha pasado.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 26px; color: #ff4b6b; margin-top: 30px; font-family: 'serif';">
            ¿Aceptarías ser mi San Valentín hoy, mañana y siempre? 🌹
        </p>
        <p class="firma">Con todo mi amor, Justin</p>
    </div>
    """, unsafe_allow_html=True)

# CARGA DE LA FOTO (Asegúrate de que se llame foto.jpg en tu GitHub)
try:
    st.image("foto.jpg", use_container_width=True)
except:
    st.info("Cargando nuestra foto especial... ❤️")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ, MIL VECES SÍ! 😍"):
        st.balloons()
        st.snow() # Un efecto extra de magia
        st.success("¡Gracias por hacerme el hombre más afortunado! Prometo cuidarte y amarte cada segundo. ¡Te amo! ❤️")

with col2:
    if st.button("No... 😢"):
        frases = [
            "¿Estás segura? Creo que el botón rosa tiene mejores premios... ✨",
            "¡Ups! Este botón parece estar bloqueado por el destino. 😊",
            "Piénsalo bien, pequeña Lubaloo... ¡tengo muchas sorpresas para ti! 🍫",
            "Mi corazón me dice que tu dedo buscaba el otro botón. 🌹",
            "¡Inténtalo de nuevo! El amor siempre da segundas oportunidades. ❤️"
        ]
        st.warning(random.choice(frases))

# Pie de página elegante
st.markdown("---")
st.markdown("<p style='text-align: center; color: white; font-size: 16px; font-weight: bold;'>Para: Lubaloo | De: Justin — Febrero 2026</p>", unsafe_allow_html=True)
