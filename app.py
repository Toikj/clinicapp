import streamlit as st
from datetime import date

# Configuración de la página
st.set_page_config(page_title="ClinicApp", layout="centered")

# Un poquito de "magia" visual para acercarnos a tu estilo
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { border-radius: 20px; border: none; box-shadow: 5px 5px 15px #d1d1d1, -5px -5px 15px #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🩺 ClinicApp")
st.subheader("Gestión de Consultorio")

# Barra lateral de navegación
menu = st.sidebar.radio("Ir a:", ["Calendario", "Pacientes", "Finanzas"])

if menu == "Calendario":
    st.write("### 📅 Agenda Semanal")
    d = st.date_input("Selecciona una fecha", date.today())
    st.info(f"Viendo turnos para el día: {d}")
    
    # Buscador de pacientes para agendar
    pacientes_ficticios = ["Cristina Hernandez", "Fede Lang", "Martin Pago", "Lucia Garcia"]
    busqueda = st.selectbox("Buscar paciente para agendar:", [""] + pacientes_ficticios)
    
    if busqueda:
        st.success(f"Agendando a: {busqueda} para las 15:00hs")
        if st.button("Enviar WhatsApp de confirmación"):
            st.write(f"📲 Abriendo chat con {busqueda}...")

elif menu == "Pacientes":
    st.write("### 👥 Fichas de Pacientes")
    st.text_input("Buscar por nombre...")
    st.button("+ Nuevo Paciente")

elif menu == "Finanzas":
    st.write("### 💰 Control de Caja")
    st.metric(label="Ganancia Mensual", value="$120.500", delta="+15%")
    st.warning("Pacientes con pagos pendientes: 3")
