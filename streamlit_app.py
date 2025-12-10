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
        "-  Puntos: Puntos donde se registraron formularios virtuales\n"
    )

    # Ruta al ZIP
    zip_path = "mapa_empadronamiento.zip"

    if os.path.exists(zip_path):

        import zipfile

        try:
            # Abrir ZIP y leer el HTML internamente
            with zipfile.ZipFile(zip_path, "r") as z:
                with z.open("mapa_empadronamiento.html") as f:
                    html_content = f.read().decode("utf-8")

            # Mostrar el mapa en Streamlit
            components.html(html_content, height=800, scrolling=True)

        except Exception as e:
            st.error(f"Error leyendo el archivo ZIP: {e}")

    else:
        st.error(f"No se encontró '{zip_path}'. Súbelo a la carpeta data/.")


