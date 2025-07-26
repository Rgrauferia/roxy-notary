# Roxy Notary™ – Versión Final para Grau Service LLC
# Funciones: Firma digital, formularios legales, historial, email, imagen de Roxy, logo y branding

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

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Roxy Notary™ – Grau Service LLC", layout="centered")
db = TinyDB("roxy_notary_historial.json")

# --- CABECERA VISUAL ---
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://i.postimg.cc/15LrsMqT/roxy-avatar.png", width=65)
with col2:
    st.markdown("## 🦁 Roxy Notary™ – Grau Service LLC")
    st.caption("Asistente notarial inteligente con visión del futuro · Florida · 🤖")

# --- INFORMACIÓN NOTARIAL ---
st.markdown("""
**Notary Public:** Roberto A. Grau  
**State of Florida**  
**Commission #:** HH697701  
**Expires:** July 13, 2029  
""")

# --- FORMULARIO ---
st.subheader("📄 Generar documento notariado")
with st.form("notary_form"):
    nombre_cliente = st.text_input("Nombre del cliente")
    tipo_documento = st.selectbox("Tipo de documento", [
        "Affidavit", "Power of Attorney", "Family Claim", "Letter of Consent", "Otro"
    ])
    detalles = st.text_area("Detalles del documento")
    fecha = st.date_input("Fecha del documento", value=date.today())

    st.markdown("✍️ Firma con el dedo del cliente:")
    canvas_result = st_canvas(
        stroke_width=2,
        stroke_color="#000000",
        background_color="#ffffff",
        update_streamlit=True,
        height=150,
        drawing_mode="freedraw",
        key="canvas_firma"
    )

    enviar = st.form_submit_button("📎 Generar documento")

# --- GENERAR DOCUMENTO ---
if enviar and nombre_cliente and detalles:
    firma_img = canvas_result.image_data
    firma_buffer = io.BytesIO()
    if firma_img is not None:
        firma_pil = Image.fromarray(firma_img.astype("uint8"))
        firma_pil.save(firma_buffer, format="PNG")
        firma_buffer.seek(0)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"""
Documento: {tipo_documento}
Cliente: {nombre_cliente}
Fecha: {fecha.strftime('%B %d, %Y')}
Detalles: {detalles}

Sello Notarial: Roberto A. Grau – Comm. HH697701 (Exp. 07/13/2029)
""")

    # Firma del cliente
    if firma_img is not None:
        firma_path = "firma_cliente.png"
        with open(firma_path, "wb") as f:
            f.write(firma_buffer.read())
        pdf.image(firma_path, x=10, y=pdf.get_y() + 10, w=60)

    # Guardar PDF
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    st.success("✅ Documento notarial generado con éxito.")
    st.download_button("📄 Descargar PDF", data=pdf_output, file_name="documento_roxy.pdf", mime="application/pdf")

    # Guardar en historial
    db.insert({
        "cliente": nombre_cliente,
        "tipo": tipo_documento,
        "fecha": fecha.isoformat(),
        "detalles": detalles
    })

    # Botón de enviar por email
    st.markdown("### 📤 Enviar documento por email")
    email_destino = st.text_input("Correo del cliente:")
    if st.button("✉️ Enviar ahora"):
        remitente = "roxy@grau360.com"
        asunto = f"Documento Notarial: {tipo_documento}"
        cuerpo = f"Hola {nombre_cliente},\nAdjunto el documento solicitado.\n\nRoxy Notary – Grau Service LLC"

        mensaje = MIMEMultipart()
        mensaje["From"] = remitente
        mensaje["To"] = email_destino
        mensaje["Subject"] = asunto
        mensaje.attach(MIMEText(cuerpo, "plain"))
        mensaje.attach(MIMEApplication(pdf_output.getvalue(), Name="documento_roxy.pdf"))

        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(remitente, "AQUI_TU_PASSWORD")
            servidor.sendmail(remitente, email_destino, mensaje.as_string())
            servidor.quit()
            st.success("📬 Documento enviado exitosamente al correo.")
        except Exception as e:
            st.error(f"Error al enviar: {e}")

# --- HISTORIAL ---
st.sidebar.header("📚 Historial de documentos")
registros = db.all()
for r in registros[::-1][:5]:
    st.sidebar.markdown(f"- {r['cliente']} · {r['tipo']} · {r['fecha']}")

# --- CONTACTO ---
st.sidebar.markdown("---")
st.sidebar.markdown("📬 Contacto: **roxy@grau360.com**")
