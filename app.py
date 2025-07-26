import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Roxy Notary™", layout="centered")

st.title("📜 Roxy Notary™ – Florida Notary App")
st.image("https://i.imgur.com/q1h5RRP.png", width=120)

st.markdown("""
**Notary Public:** Roberto A. Grau  
**State of Florida**  
**Commission #:** HH697701  
**Expires:** July 13, 2029  
""")

st.subheader("📄 Generar documento notariado")
with st.form("notary_form"):
    nombre_cliente = st.text_input("Nombre del cliente")
    tipo_documento = st.selectbox("Tipo de documento", ["Affidavit", "Power of Attorney", "Family Claim", "Consent Form", "Otro"])
    detalles = st.text_area("Detalles del documento")
    fecha = st.date_input("Fecha", value=datetime.today())
    firmar = st.form_submit_button("Generar PDF")

if firmar and nombre_cliente and detalles:
    st.success("✅ Documento notariado generado exitosamente.")
    st.markdown(f"""
    **Documento:** {tipo_documento}  
    **Cliente:** {nombre_cliente}  
    **Fecha:** {fecha.strftime('%B %d, %Y')}  
    **Sello Notarial:** Roberto A. Grau – Comm. HH697701 (Exp. 07/13/2029)  
    """)
    st.download_button("📥 Descargar PDF Simulado", data="(Contenido del documento)", file_name="notary_document.pdf")
elif firmar:
    st.warning("❗Por favor completa todos los campos.")
