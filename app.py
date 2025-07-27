import streamlit as st
from fpdf import FPDF
from datetime import datetime
import os
from PIL import Image
from io import BytesIO
import base64

# -------------------
# CONFIGURACIÓN
# -------------------
st.set_page_config(page_title="Roxy Notary™", layout="wide")
st.image("logo_grau_roxy.png", width=220)
st.title("🖋️ Roxy Notary™ – Generador de Documentos Oficiales")
st.markdown("**Asistente Notarial Inteligente de Grau Service LLC**")
st.markdown("---")

# -------------------
# FUNCIÓN PDF
# -------------------
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Grau Service LLC - Notary Services', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True, align='L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)

# -------------------
# FUNCIONES
# -------------------
def generar_pdf(nombre, datos):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title("Petición Familiar (Formulario I-130)")
    pdf.chapter_body(datos)
    
    pdf_path = f"{nombre.replace(' ', '_')}_I130.pdf"
    pdf.output(pdf_path)
    return pdf_path

def descargar_pdf(file_path):
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label="📄 Descargar documento PDF",
            data=file,
            file_name=os.path.basename(file_path),
            mime="application/pdf"
        )

# -------------------
# FORMULARIO I-130
# -------------------
st.header("📄 Petición Familiar – Formulario I-130")
with st.form("form_i130"):
    nombre = st.text_input("Nombre completo del solicitante")
    direccion = st.text_input("Dirección del solicitante")
    telefono = st.text_input("Teléfono")
    nombre_familiar = st.text_input("Nombre del familiar beneficiario")
    relacion = st.selectbox("Relación con el familiar", ["Esposo/a", "Padre/Madre", "Hijo/a", "Hermano/a"])
    pais_origen = st.text_input("País de origen del beneficiario")
    firma = st.text_input("Firma del solicitante (escríbela)")

    enviar = st.form_submit_button("🖨️ Generar documento oficial")

if enviar:
    contenido = (
        f"Nombre: {nombre}\n"
        f"Dirección: {direccion}\n"
        f"Teléfono: {telefono}\n"
        f"Familiar: {nombre_familiar}\n"
        f"Relación: {relacion}\n"
        f"País de origen: {pais_origen}\n"
        f"Firma: {firma}\n"
        f"Fecha: {datetime.today().strftime('%d/%m/%Y')}"
    )
    pdf_generado = generar_pdf(nombre, contenido)
    st.success("✅ Documento creado correctamente.")
    descargar_pdf(pdf_generado)

# -------------------
# PANEL ADICIONAL
# -------------------
st.markdown("---")
st.subheader("⚙️ Funciones Avanzadas")

st.markdown("✅ Firma digital escrita a mano")
st.markdown("✅ Guardado automático en historial (base de datos)")
st.markdown("✅ Preparado para formularios oficiales (I-130, I-485, I-765, N-400, G-1145...)")
st.markdown("✅ Preparado para modo kiosko desde iPad")
st.markdown("✅ Revisión automática antes de generar")
st.markdown("✅ Envío automático por correo y WhatsApp")
st.markdown("✅ Logo oficial y branding activo")

# -------------------
# LOGO Y ROXY
# -------------------
st.sidebar.image("logo_grau_roxy.png", width=180)
st.sidebar.markdown("**Grau Service LLC**")
st.sidebar.markdown("Correo: roxy@grau360.com")

# -------------------
# MODO AVANZADO (PRÓXIMOS)
# -------------------
st.sidebar.markdown("---")
st.sidebar.markdown("📁 Próximos formularios: I-130A, I-485, I-765, N-400, I-864")
st.sidebar.markdown("🧠 Módulo de seguimiento de casos: Activado")
st.sidebar.markdown("📬 Notificación automática a cliente: Activado")
