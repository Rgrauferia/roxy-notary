# roxy_notary.py – Módulo principal de Roxy Notary™ con formularios oficiales, selector de idioma y diseño optimizado

import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import requests
import datetime
from tinydb import TinyDB, Query
import os

# Base de datos local
db = TinyDB("roxy_notary_db.json")

# Configuración de la app
st.set_page_config(page_title="Roxy Notary™ – Grau Service LLC", layout="centered")

# Logos y diseño
st.markdown("""<style>
    .css-1q8dd3e {padding-top: 0rem;}
    .css-18ni7ap {padding-top: 1rem;}
</style>""", unsafe_allow_html=True)

# Logo + Imagen de Roxy
col1, col2 = st.columns([1, 3])
with col1:
    logo_url = "https://grau360.s3.amazonaws.com/logo_grau_roxy.png"
    img = Image.open(requests.get(logo_url, stream=True).raw)
    st.image(img, width=130)
with col2:
    st.title("Roxy Notary™")
    st.caption("Tu asistente notarial inteligente")

# Idioma
idioma = st.selectbox("🌐 Select Language / Selecciona idioma", ["English", "Español"])

# Ingreso de datos del cliente
st.subheader("📄 Información del Cliente / Client Information")

with st.form("form_datos"):
    nombre = st.text_input("Nombre completo / Full Name")
    direccion = st.text_input("Dirección / Address")
    telefono = st.text_input("Teléfono / Phone")
    correo = st.text_input("Correo electrónico / Email")
    tipo_formulario = st.selectbox("Tipo de documento / Document Type", [
        "I-130 Petition for Alien Relative",
        "I-130A – Supplemental Info",
        "I-765 – Work Permit",
        "I-485 – Adjustment of Status",
        "N-400 – Naturalization",
        "Green Card Renewal – I-90"
    ])
    submit = st.form_submit_button("Generar documento oficial")

# Generador PDF básico (simulado para pruebas)
if submit and nombre and direccion and telefono and correo:
    st.success("✅ Documento generado correctamente.")
    ruta_salida = f"{tipo_formulario.replace(' ', '_')}_{nombre.replace(' ', '_')}.pdf"

    with open("template_blank.pdf", "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.add_metadata({
            "/Author": "Roxy Notary™",
            "/Title": tipo_formulario,
            "/Subject": "Documento generado por IA"
        })

        with open(ruta_salida, "wb") as output:
            writer.write(output)

    with open(ruta_salida, "rb") as f:
        st.download_button("📥 Descargar documento PDF", f, file_name=ruta_salida, mime="application/pdf")

    db.insert({
        "nombre": nombre,
        "documento": tipo_formulario,
        "fecha": str(datetime.date.today()),
        "correo": correo,
        "telefono": telefono
    })

else:
    st.info("Completa todos los campos para generar el documento.")

# Certificación notarial al pie (en inglés)
st.markdown("---")
st.markdown("**Notary Certification**")
st.markdown("""
I certify that on this date, I personally verified the identity of the above-named individual, and I notarized the document in accordance with the laws of the State of Florida.

**Name:** Roberto Grau  
**Commission Number:** FL12345678  
**My Commission Expires:** 12/31/2027
""")

# Botón para volver al inicio (reinicio rápido)
if st.button("🔄 Volver al inicio"):
    st.experimental_rerun()
