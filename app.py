import streamlit as st
from PIL import Image
import datetime

# --------------------------
# CONFIGURACIÓN GENERAL
# --------------------------
st.set_page_config(page_title="Roxy Notary™", layout="centered")

# --------------------------
# LOGO Y BIENVENIDA
# --------------------------
logo = Image.open("415FBB81-11A5-4C5D-965E-8F6EE4526CA1.png")
st.image(logo, width=250)

st.title("📜 Roxy Notary™")
st.markdown("### Asistente notarial inteligente en Florida")
st.markdown("Firma, sello y generación automática de documentos legales con IA.")

st.divider()

# --------------------------
# MENÚ PRINCIPAL
# --------------------------
menu = st.selectbox("Selecciona una función:", [
    "Inicio", 
    "Generar Documento Notarial",
    "Firmar Digitalmente",
    "Validar Identidad",
    "Ayuda"
])

# --------------------------
# SECCIONES
# --------------------------
if menu == "Inicio":
    st.success("Bienvenido a Roxy Notary™. Selecciona una opción en el menú para comenzar.")

elif menu == "Generar Documento Notarial":
    st.subheader("📝 Crear Documento Notarial")
    nombre = st.text_input("Nombre completo del cliente")
    tipo_doc = st.selectbox("Tipo de documento", ["Carta Poder", "Afidávit", "Declaración Jurada", "Reclamación Familiar"])
    fecha = st.date_input("Fecha del documento", datetime.date.today())

    if st.button("Generar Documento"):
        if nombre:
            st.success(f"✅ Documento '{tipo_doc}' generado para {nombre} el {fecha.strftime('%d/%m/%Y')}")
            st.info("🔐 Próximo paso: Firma y validación.")
        else:
            st.error("Por favor, escribe el nombre del cliente.")

elif menu == "Firmar Digitalmente":
    st.subheader("✍️ Firma Digital")
    st.warning("Esta función estará disponible en la próxima versión.")

elif menu == "Validar Identidad":
    st.subheader("🛂 Validación de Identidad")
    st.warning("Esta función estará integrada con verificación por selfie y documentos.")

elif menu == "Ayuda":
    st.subheader("📞 Centro de Ayuda")
    st.markdown("Si tienes dudas o necesitas asistencia, puedes escribir directamente a:")
    st.markdown("- WhatsApp: [📱 +1 (267) 634-4137](https://wa.me/12676344137)")
    st.markdown("- Email: grauservice.llg@gmail.com")

# --------------------------
# PIE DE PÁGINA
# --------------------------
st.divider()
st.caption("© 2025 Roxy Notary™ · Desarrollado para Grau Service LLC")
