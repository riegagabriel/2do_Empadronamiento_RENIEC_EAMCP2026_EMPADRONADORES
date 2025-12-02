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
tab3, = st.tabs(["🗺️ Mapa de Empadronamiento"])

# ===========================================
# 🗺️ TAB 3: MAPA DE EMPADRONAMIENTO
# ===========================================
with tab3:
    st.subheader("🗺️ Mapa de Empadronamiento")

    st.markdown(
        "📝 **Leyenda:**\n"
        "- Puntos: Puntos donde se registraron formularios virtuales\n"
    )

    mapa_path = "mapa_empadronamiento.html"

    if os.path.exists(mapa_path):
        with open(mapa_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        components.html(html_content, height=800, scrolling=True)

    else:
        st.error(f"No se encontró el archivo '{mapa_path}'.")
        st.info("Guarda el archivo como 'mapa_empadronamiento.html' en el mismo directorio.")
