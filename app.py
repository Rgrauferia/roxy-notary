import streamlit as st
import datetime
import base64
from fpdf import FPDF
from tinydb import TinyDB, Query

# ------------------ CONFIGURACIÓN INICIAL ------------------ #
st.set_page_config(page_title="Roxy Notary™ | Grau Service LLC", layout="wide")
st.title("🦁 Roxy Notary™ – Grau Service LLC")
st.markdown("### 👩‍💼 Tu asistente notarial inteligente")
db = TinyDB("historial_documentos.json")

# ------------------ FUNCIONES ------------------ #
def generar_pdf(nombre_cliente, tipo_documento, contenido):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, contenido)
    nombre_archivo = f"{tipo_documento.replace(' ', '_')}_{nombre_cliente.replace(' ', '_')}.pdf"
    pdf.output(nombre_archivo)
    return nombre_archivo

def guardar_en_historial(nombre_cliente, tipo_documento, contenido):
    db.insert({
        "cliente": nombre_cliente,
        "documento": tipo_documento,
        "contenido": contenido,
        "fecha": str(datetime.datetime.now())
    })

def mostrar_historial():
    st.subheader("📚 Historial de Documentos")
    historial = db.all()
    for doc in historial[::-1]:
        with st.expander(f"{doc['fecha']} – {doc['cliente']} – {doc['documento']}"):
            st.code(doc["contenido"])

# ------------------ FORMULARIO PRINCIPAL ------------------ #
st.subheader("📝 Crear documento notarial")

nombre_cliente = st.text_input("Nombre del Cliente")
tipo_documento = st.selectbox("Tipo de Documento", [
    "Affidavit",
    "Carta de Poder",
    "Reclamación Familiar (I-130)",
    "Notificación Legal",
    "G-1145 Notificación USCIS",
    "Otro"
])
contenido_documento = st.text_area("Contenido del documento")

if st.button("✅ Generar Documento"):
    if nombre_cliente and contenido_documento:
        archivo_pdf = generar_pdf(nombre_cliente, tipo_documento, contenido_documento)
        guardar_en_historial(nombre_cliente, tipo_documento, contenido_documento)
        st.success(f"Documento '{tipo_documento}' generado para {nombre_cliente}")
        with open(archivo_pdf, "rb") as f:
            pdf_data = f.read()
        b64 = base64.b64encode(pdf_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{archivo_pdf}">📥 Descargar PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Completa todos los campos.")

# ------------------ HISTORIAL ------------------ #
mostrar_historial()

# ------------------ IDENTIDAD ------------------ #
st.markdown("---")
st.image("https://i.imgur.com/2xjQk9j.png", width=100)  # Logo del león
st.markdown("**Asistente Roxy Notary™ – powered by Grau Service LLC**")
st.markdown("📧 roxy@grau360.com | 📞 267-634-4137")
