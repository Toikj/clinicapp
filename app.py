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
import streamlit as st
import urllib.parse

st.set_page_config(page_title="ClinicApp", layout="wide")

# Inicializar nuestra "base de datos" temporal
if 'pacientes' not in st.session_state:
    st.session_state['pacientes'] = [
        {"nombre": "Cristina Hernandez", "tel": "5491122334455", "pago": "Particular"},
        {"nombre": "Fede Lang", "tel": "5491155667788", "pago": "Obra Social"}
    ]

st.title("🩺 ClinicApp")

menu = st.sidebar.selectbox("Navegación", ["Calendario", "Fichas de Pacientes", "Finanzas"])

if menu == "Calendario":
    st.header("📅 Agenda de Turnos")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Nuevo Turno")
        nombres = [p['nombre'] for p in st.session_state['pacientes']]
        paciente_sel = st.selectbox("Seleccionar Paciente", nombres)
        fecha = st.date_input("Fecha")
        hora = st.time_input("Hora")
        
        if st.button("Confirmar y Avisar por WhatsApp"):
            # Buscar el teléfono del paciente seleccionado
            tel = next(p['tel'] for p in st.session_state['pacientes'] if p['nombre'] == paciente_sel)
            mensaje = f"Hola {paciente_sel}, te confirmo nuestro turno el día {fecha} a las {hora} hs."
            link = f"https://wa.me/{tel}?text={urllib.parse.quote(mensaje)}"
            st.markdown(f'[Click aquí para enviar mensaje 📲]({link})')

elif menu == "Fichas de Pacientes":
    st.header("👥 Gestión de Pacientes")
    
    with st.expander("➕ Agregar Nuevo Paciente"):
        nuevo_nom = st.text_input("Nombre Completo")
        nuevo_tel = st.text_input("Teléfono (con código de país, ej: 549...)")
        if st.button("Guardar Paciente"):
            st.session_state['pacientes'].append({"nombre": nuevo_nom, "tel": nuevo_tel, "pago": "Particular"})
            st.success("¡Paciente guardado!")

    st.write("### Lista de Pacientes")
    for p in st.session_state['pacientes']:
        st.info(f"👤 **{p['nombre']}** - Tel: {p['tel']}")
