import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Lubaloo ❤️", page_icon="🌹")

# Estilos personalizados: Fondo de CORAZONES y diseño de cristal
st.markdown("""
    <style>
    /* Imagen de fondo (Corazones de San Valentín) */
    .stApp {
        /* Nueva imagen de fondo con temática de corazones */
        background-image: url("https://images.unsplash.com/photo-1612452830763-568fb16926bb?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* El fondo se queda fijo al hacer scroll */
    }
    
    /* Contenedor de la carta con efecto cristal (Glassmorphism) */
    .carta-contenedor {
        background-color: rgba(255, 255, 255, 0.90); /* Un poco más opaco para que se lea bien sobre los corazones */
        padding: 40px;
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.7);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        color: #5d0e24;
        margin-bottom: 25px;
        text-align: justify;
        backdrop-filter: blur(8px); /* Efecto borroso detrás de la carta */
    }
    
    .titulo-nuevo {
        color: #c9184a !important;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        text-align: center;
        font-family: 'serif';
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 30px;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 15px;
        border-radius: 25px;
        border: 2px solid #ff4b6b;
    }

    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 4em;
        background-color: #ff4b6b;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        box-shadow: 0px 5px 15px rgba(255, 75, 107, 0.5);
        transition: transform 0.2s, background-color 0.2s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #d6284a; /* Un rojo más intenso al pasar el mouse */
    }

    .firma {
        text-align: right;
        font-style: italic;
        font-weight: bold;
        color: #c9184a;
        margin-top: 25px;
        font-size: 20px;
    }
    
    .musica-texto {
        text-align: center;
        color: #ffffff;
        font-weight: bold;
        margin-bottom: 15px;
        font-size: 18px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        background-color
