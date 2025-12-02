import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import streamlit.components.v1 as components

# ========================
# CONFIGURACIÓN GENERAL
# ========================
st.set_page_config(
    page_title="Dashboard RENIEC – Empadronamiento",
    layout="wide"
)

st.title("📊 2do Empadronamiento")
st.markdown("Mapa de avance de los Municipios de Centros Poblados (MCP)")

# ========================
# PESTAÑAS
# ========================
tab3 = st.tabs([
    "🗺️ Mapa de Empadronamiento"
])

# ===========================================
# 🗺️ TAB 3: MAPA DE EMPADRONAMIENTO
# ===========================================
with tab3:
    st.subheader("🗺️ Mapa de Empadronamiento")
    
    # Texto de leyenda
    st.markdown(
        "📝 **Leyenda:**\n"
        "- Puntos: Puntos donde se registraron formularios virutales\n"
    )
    
    # Ruta del archivo HTML del mapa
    mapa_path = "mapa_empadronamiento.html"
    
    # Verificar si el archivo existe
    if os.path.exists(mapa_path):
        # Leer el contenido del archivo HTML
        with open(mapa_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Mostrar el mapa usando components.html
        components.html(html_content, height=800, scrolling=True)
        
    else:
        st.error(f"No se encontró el archivo '{mapa_path}'. Asegúrate de que el archivo esté en la misma carpeta que el script de Streamlit.")
        st.info("El mapa debe estar guardado como 'mapa_empadronamiento.html' en el directorio principal de la aplicación.")

