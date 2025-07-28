import streamlit as st
from PIL import Image
from fpdf import FPDF
import datetime

# -------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------
st.set_page_config(page_title="Roxy Notary™", layout="centered")

# -------------------------------
# LOGO E IDENTIDAD VISUAL
# -------------------------------
col1, col2 = st.columns([1, 5])
with col1:
    try:
        img = Image.open("logo.png")
        st.image(img, width=90)
    except:
        st.warning("Logo no disponible")
with col2:
    st.title("Roxy Notary™")
    st.caption("Asistente notarial inteligente para Florida")

# -------------------------------
# SELECTOR DE IDIOMA
# -------------------------------
idioma = st.selectbox("🌐 Language / Idioma", ["Español", "English"])

# -------------------------------
# FORMULARIO NOTARIAL
# -------------------------------
st.header("📄 " + ("Generar documento notarial" if idioma == "Español" else "Generate Notarial Document"))

nombre_cliente = st.text_input("Nombre del firmante" if idioma == "Español" else "Signer Name")
documento = st.text_area("Descripción del documento" if idioma == "Español" else "Document Description")
fecha_actual = datetime.date.today().strftime("%B %d, %Y")

firmar = st.button("🔏 Generar y firmar documento" if idioma == "Español" else "🔏 Generate and Sign")

# -------------------------------
# GENERACIÓN DE PDF NOTARIAL
# -------------------------------
if firmar and nombre_cliente and documento:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Roxy Notary™ – Florida Notarial Certificate", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, f"Signed by: {nombre_cliente}")
    pdf.multi_cell(0, 10, f"Document: {documento}")
    pdf.multi_cell(0, 10, f"Date: {fecha_actual}")
    pdf.ln(10)

    if idioma == "Español":
        pdf.multi_cell(0, 10, f"Certifico que el(los) firmante(s) fue(ron) identificado(s) satisfactoriamente por mí, "
                              f"y que firmó(aron) este documento el día {fecha_actual} en el Estado de Florida.")
    else:
        pdf.multi_cell(0, 10, f"I certify that the signer(s) was/were satisfactorily identified by me and signed "
                              f"this document on {fecha_actual} in the State of Florida.")

    pdf.ln(10)
    pdf.cell(0, 10, "Roberto A. Grau", ln=True)
    pdf.cell(0, 10, "Notary Public – State of Florida", ln=True)
    pdf.cell(0, 10, "Comm # HH697701 · Expires 07/13/2029", ln=True)

    # Guardar PDF
    nombre_pdf = f"RoxyNotary_{nombre_cliente.replace(' ', '_')}.pdf"
    pdf.output(nombre_pdf)

    # Mostrar éxito y enlace
    with open(nombre_pdf, "rb") as file:
        st.success("✅ Documento generado con éxito")
        st.download_button(
            label="📥 Descargar documento notariado",
            data=file,
            file_name=nombre_pdf,
            mime="application/pdf"
        )
else:
    st.info("📝 Ingresa todos los datos para generar el documento")
