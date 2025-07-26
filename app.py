# Roxy Notary™ – Versión Final para Grau Service LLC
# Funciones: Firma digital, formularios legales, historial, email/WhatsApp, base de datos, imagen activa
# Asistente IA: Roxy – Imagen visible, empresa activa

import streamlit as st
from fpdf import FPDF
from datetime import date, datetime
from streamlit_drawable_canvas import st_canvas
from tinydb import TinyDB, Query
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import io

# Configuración de página
st.set_page_config(page_title="Roxy Notary™ – Grau Service LLC", layout="centered")

# Base de datos local
db = TinyDB("roxy_notary_historial.json")

# --- CABECERA VISUAL ---
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://i.postimg.cc/15LrsMqT/roxy-avatar.png", width=65)
with col2:
    st.markdown("## 🦁 Roxy Notary™ – Grau Service LLC")
    st.caption("Asistente notarial inteligente con visión del futuro · Florida · 📍")

# --- FORMULARIO DE CLIENTE ---
st.subheader("📄 Crear documento notarial")
nombre = st.text_input("Nombre completo del cliente")
servicio = st.selectbox("Tipo de servicio", ["Affidavit", "Consentimiento", "Testimonio", "Contrato", "Otro"])
comentarios = st.text_area("Detalles adicionales (opcional)")
firmar = st.checkbox("¿Desea firmar el documento ahora?")

# --- LIENZO PARA FIRMA ---
st.markdown("### ✍️ Firma digital del cliente")
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.0)",
    stroke_width=2,
    stroke_color="#000000",
    background_color="#ffffff",
    height=150,
    width=400,
    drawing_mode="freedraw",
    key="firma"
)

# --- BOTÓN PARA GUARDAR ---
if st.button("✅ Generar documento"):
    if nombre and servicio and canvas_result.image_data is not None:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Documento Notarial - {servicio}", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Nombre del Cliente: {nombre}", ln=True)
        pdf.cell(200, 10, txt=f"Servicio: {servicio}", ln=True)
        pdf.multi_cell(200, 10, txt=f"Comentarios: {comentarios}", align="L")
        pdf.cell(200, 10, txt=f"Fecha: {date.today()}", ln=True)

        # Guardar PDF temporalmente
        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        # Guardar en base de datos
        db.insert({
            "nombre": nombre,
            "servicio": servicio,
            "comentarios": comentarios,
            "fecha": str(date.today())
        })

        st.success("✅ Documento generado correctamente")
        st.download_button("📥 Descargar PDF", data=pdf_output, file_name="documento_roxy.pdf")

    else:
        st.warning("Completa los datos y realiza la firma para continuar.")

# --- HISTORIAL ---
st.markdown("---")
st.subheader("📚 Historial de documentos")
historial = db.all()
for entry in historial[::-1][:5]:
    st.markdown(f"• **{entry['nombre']}** – {entry['servicio']} ({entry['fecha']})")

# --- CONTACTO ---
st.markdown("---")
st.markdown("📧 Contacto: `roxy@grau360.com` · WhatsApp: [Click aquí](https://wa.me/12676344137)")
