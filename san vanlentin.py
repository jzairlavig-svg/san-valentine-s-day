import streamlit as st
import random

# --- 1. CONFIGURACIÓN (OBLIGATORIO PRIMERA LÍNEA) ---
st.set_page_config(page_title="Para Lubaloo ❤️", page_icon="🌹", layout="centered")

# --- 2. ESTILOS CSS (FONDO SEGURO SIN IMAGEN EXTERNA) ---
st.markdown("""
    <style>
    /* FONDO DEGRADADO: Carga instantánea y nunca falla */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        background-attachment: fixed;
    }
    
    /* CAJA DE LA CARTA */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 20px;
        border: 4px solid white;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
        color: #880d1e; /* Color de texto oscuro para que se lea bien */
        margin-bottom: 25px;
        text-align: justify;
    }
    
    /* TÍTULO */
    h1 {
        color: #d61c4e !important;
        text-align: center;
        font-family: 'serif';
        text-shadow: 2px 2px 0px white;
    }

    /* BOTONES */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 50px;
        background-color: #ff2e63;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }
    
    .stButton>button:hover {
        background-color: #c70d3a;
        transform: scale(1.02);
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
        padding: 8px 15px;
        border-radius: 20px;
        color: #ff2e63;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Ajuste de imagen y video */
    img { border-radius: 15px; }
    iframe { border-radius: 15px; box-shadow: 0px 5px 15px rgba(0,0,0,0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTENIDO VISUAL ---

st.title("🌹 Una pregunta desde mi corazón 🌹")

# CARTA
st.markdown(f"""
    <div class="carta-contenedor">
        <p style="font-size: 20px; font-weight: bold; color: #d61c4e;">Mi adorada Lubaloo,</p>
        <p style="font-size: 18px; line-height: 1.6;">
            Parece que fue ayer cuando empezamos este camino, y ya han pasado <b>10 maravillosos meses</b>. 
            En este tiempo, no solo te has convertido en mi novia, sino en mi mejor amiga, en mi refugio y en la razón por la que siempre tengo una sonrisa al despertar. <br><br>
            A tu lado, he aprendido que el amor no es perfecto, pero que contigo se siente real, puro y lleno de luz. 
            Gracias por cada risa, por cada palabra de apoyo cuando las cosas se ponen difíciles y por enseñarme a ser una mejor versión de mí mismo. 
            Eres la persona más especial que conozco y cada día que pasa me convenzo más de la suerte que tengo de tenerte.<br><br>
            Se acerca <b>San Valentín</b>, un día que celebra lo que nosotros vivimos a diario. Por eso, no quería que fuera una fecha cualquiera. 
            Quiero que sea un momento para recordarte cuánto te amo y lo mucho que deseo seguir caminando de tu mano.
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 24px; color: #ff2e63; margin-top: 20px;">
            ¿Me harías el honor de ser mi San Valentín? 🌹
        </p>
        <p class="firma">Con todo mi amor, Justin</p>
    </div>
    """, unsafe_allow_html=True)

# MÚSICA
c1, c2, c3 = st.columns([1, 6, 1])
with c2:
    st.markdown("<div style='text-align: center; margin-bottom: 10px;'><span class='musica-texto'>🎵 Dale play a nuestra canción...</span></div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=1iK-ttRjV-E")

st.write("") # Espacio vacío

# FOTO (Manejo de errores para evitar pantalla blanca)
try:
    st.image("foto.jpg", caption="Nosotros ❤️", use_container_width=True) # Probamos comando nuevo
except:
    try:
        st.image("foto.jpg", caption="Nosotros ❤️", use_column_width=True) # Probamos comando viejo si el nuevo falla
    except:
        st.error("⚠️ No se pudo cargar la foto 'foto.jpg'. Verifica el nombre en GitHub.")

st.write("") # Espacio vacío

# BOTONES
col1, col2 = st.columns(2)
with col1:
    if st.button("¡SÍ, ACEPTO! 😍"):
        st.balloons()
        st.snow()
        st.success("¡Me haces el hombre más feliz del mundo! ¡Te amo demasiado! ❤️")

with col2:
    if st.button("No... 😢"):
        st.warning("Opción no disponible. ¡El destino dice que sí! 😊")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #880d1e;'>Para: Lubaloo | De: Justin — Febrero 2026</div>", unsafe_allow_html=True)
