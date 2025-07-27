import streamlit as st
from PIL import Image
import requests
import base64
import os

st.set_page_config(page_title="Roxy Notary™ – Grau Service LLC", layout="wide")

# Mostrar logo desde URL
logo_url = "https://grau360.s3.amazonaws.com/logo_grau_roxy.png"
img = Image.open(requests.get(logo_url, stream=True).raw)
st.image(img, width=200)

st.title("📄 Roxy Notary™ – Documentos Oficiales Automatizados")
st.markdown("Bienvenido a Roxy Notary™, tu asistente de confianza para generar formularios y documentos legales listos para firmar y enviar.")

# ---------------------
# Función para mostrar PDF oficial
# ---------------------
def mostrar_pdf(url_pdf):
    pdf_display = f'<iframe src="{url_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# ---------------------
# Menú principal
# ---------------------
formulario = st.selectbox("Selecciona el documento que deseas generar:", [
    "Selecciona...",
    "I-130 · Petición Familiar",
    "I-130A · Información del Beneficiario",
    "I-765 · Permiso de Trabajo",
    "I-485 · Ajuste de Estatus",
    "N-400 · Ciudadanía",
    "I-90 · Renovación de Green Card"
])

st.divider()

# Mostrar PDF oficial según selección
if formulario == "I-130 · Petición Familiar":
    st.subheader("Formulario I-130 – Petición de Familiar Extranjero")
    mostrar_pdf("https://www.uscis.gov/sites/default/files/document/forms/i-130.pdf")
    st.download_button("⬇️ Descargar PDF", data=requests.get("https://www.uscis.gov/sites/default/files/document/forms/i-130.pdf").content, file_name="i-130.pdf")

elif formulario == "I-130A · Información del Beneficiario":
    st.subheader("Formulario I-130A – Información del Cónyuge")
    mostrar_pdf("https://www.uscis.gov/sites/default/files/document/forms/i-130a.pdf")
    st.download_button("⬇️ Descargar PDF", data=requests.get("https://www.uscis.gov/sites/default/files/document/forms/i-130a.pdf").content, file_name="i-130a.pdf")

elif formulario == "I-765 · Permiso de Trabajo":
    st.subheader("Formulario I-765 – Solicitud de Autorización de Empleo")
    mostrar_pdf("https://www.uscis.gov/sites/default/files/document/forms/i-765.pdf")
    st.download_button("⬇️ Descargar PDF", data=requests.get("https://www.uscis.gov/sites/default/files/document/forms/i-765.pdf").content, file_name="i-765.pdf")

elif formulario == "I-485 · Ajuste de Estatus":
    st.subheader("Formulario I-485 – Solicitud para Registrar Residencia Permanente")
    mostrar_pdf("https://www.uscis.gov/sites/default/files/document/forms/i-485.pdf")
    st.download_button("⬇️ Descargar PDF", data=requests.get("https://www.uscis.gov/sites/default/files/document/forms/i-485.pdf").content, file_name="i-485.pdf")

elif formulario == "N-400 · Ciudadanía":
    st.subheader("Formulario N-400 – Solicitud de Naturalización")
    mostrar_pdf("https://www.uscis.gov/sites/default/files/document/forms/n-400.pdf")
    st.download_button("⬇️ Descargar PDF", data=requests.get("https://www.uscis.gov/sites/default/files/document/forms/n-400.pdf").content, file_name="n-400.pdf")

elif formulario == "I-90 · Renovación de Green Card":
    st.subheader("Formulario I-90 – Reemplazo o Renovación de Tarjeta de Residente")
    mostrar_pdf("https://www.uscis.gov/sites/default/files/document/forms/i-90.pdf")
    st.download_button("⬇️ Descargar PDF", data=requests.get("https://www.uscis.gov/sites/default/files/document/forms/i-90.pdf").content, file_name="i-90.pdf")

# ---------------------
# Firma digital (modo simple)
# ---------------------
st.divider()
st.subheader("✍️ Firma digital del cliente")
firma = st.text_input("Nombre para firmar:")
if firma:
    st.markdown(f"**Firma digital registrada:** {firma}")

# ---------------------
# Botón para enviar por correo
# ---------------------
st.divider()
st.subheader("📤 ¿Qué deseas hacer con este formulario?")
col1, col2 = st.columns(2)
with col1:
    correo = st.text_input("Correo del cliente")
with col2:
    if st.button("Enviar por correo"):
        st.success(f"Formulario enviado a {correo} (función simulada)")

# ---------------------
# Footer
# ---------------------
st.divider()
st.markdown("© 2025 Roxy Notary™ · Grau Service LLC · Orlando, FL")
