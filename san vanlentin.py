import streamlit as st
import random

# --- 1. CONFIGURACIÓN (OBLIGATORIO PRIMERA LÍNEA) ---
st.set_page_config(page_title="Para Lubaloo ❤️", page_icon="🌹", layout="centered")

# --- 2. ESTILOS CSS (FONDO DE CORAZONES SEGURO) ---
st.markdown("""
    <style>
    /* FONDO DE PATRÓN DE CORAZONES (Incrustado, no falla nunca) */
    .stApp {
        background-color: #ffdde1;
        background-image: url("data:image/svg+xml,%3Csvg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M32 56C14.327 40 4 28 4 16 4 9.373 9.373 4 16 4c4.18 0 7.843 2.14 10 5.36C28.157 6.14 31.82 4 36 4c6.627 0 12 5.373 12 12 0 12-10.327 24-28 40z' fill='%23eebbc3' fill-opacity='0.6' fill-rule='evenodd'/%3E%3C/svg%3E");
        background-attachment: fixed;
    }
    
    /* CAJA DE LA CARTA (Cristal para que se lea bien sobre los corazones) */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 35px;
        border-radius: 25px;
        border: 3px solid #ffcad4;
        box-shadow: 0px 10px 25px rgba(214, 28, 78, 0.15);
        color: #880d1e;
        margin-bottom: 25px;
        text-align: justify;
        backdrop-filter: blur(5px);
    }
    
    /* TÍTULO */
    .titulo-principal {
        color: #d61c4e;
        text-align: center;
        font-family: 'serif';
        text-shadow: 2px 2px 0px white;
        background-color: rgba(255,255,255,0.8);
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 30px;
    }

    /* BOTONES */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 55px;
        background-color: #ff2e63;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #ff4b6b;
        transform: scale(1.05) translateY(-3px);
    }

    /* FIRMA */
    .firma {
        text-align: right;
        font-style: italic;
        font-weight: bold;
        color: #d61c4e;
        margin-top: 15px;
    }
    
    /* MENSAJE MÚSICA */
    .musica-texto {
        background-color: white;
        padding: 10px 20px;
        border-radius: 25px;
        color: #ff2e63;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
        border: 2px solid #ffcad4;
    }
    
    /* Ajuste de imagen y video */
    img { border-radius: 20px; border: 3px solid white; }
    iframe { border-radius: 20px; box-shadow: 0px 5px 15px rgba(0,0,0,0.2); height: 220px !important;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTENIDO VISUAL ---

st.markdown("<h1 class='titulo-principal'>🌹 Una pregunta desde mi corazón 🌹</h1>", unsafe_allow_html=True)

# CARTA
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 20px; font-weight: bold; color: #d61c4e;">Mi adorada Lubaloo,</p>
        <p style="font-size: 18px; line-height: 1.7;">
            Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. 
            En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br>
            A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. 
            Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. 
            Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br>
            Se acerca <b>San Valentín</b>, un día que celebra lo que nosotros vivimos a diario. Por eso, no quería que fuera una fecha cualquiera. 
            Quiero que sea un momento para recordarte cuánto te amo y lo mucho que deseo seguir caminando de tu mano.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 26px; color: #ff2e63; margin-top: 25px;">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
        <p class="firma">Con todo mi amor, Justin</p>
    </div>
    """, unsafe_allow_html=True)

# MÚSICA
c1, c2, c3 = st.columns([1, 6, 1])
with c2:
    st.markdown("<div style='text-align: center; margin-bottom: 15px;'><span class='musica-texto'>🎵 Dale play a nuestra canción...</span></div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=1iK-ttRjV-E")

st.write("")

# FOTO (Con protección anti-fallos)
try:
    st.image("foto.jpg", use_container_width=True)
except:
    st.warning("⚠️ No se pudo cargar la foto. Revisa que se llame 'foto.jpg' en GitHub.")

st.write("")
st.write("")

# BOTONES
col1, col2 = st.columns(2)
with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.snow()
        st.success("¡Me haces el hombre más feliz del mundo! ¡Te amo demasiado! ❤️")

with col2:
    if st.button("No... 😢"):
        st.warning("¡Esa opción está bloqueada por exceso de amor! Intenta la otra. 😊")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #880d1e; font-weight: bold;'>Para: Lubaloo | De: Justin — Febrero 2026</div>", unsafe_allow_html=True)
