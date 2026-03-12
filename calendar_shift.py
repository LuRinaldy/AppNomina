import streamlit as st
from datetime import date, time 
import calendar

st.title("Calendario mensual")

##Estados

def show_calendar():

    st.title("Calendario mensual")

    if "turnos" not in st.session_state:
        st.session_state.turnos = {}

    col1, col2 = st.columns(2)

    with col1:
        mes = st.selectbox(
            "Mes",
            list(range(1,13)),
            format_func = lambda x: calendar.month_name[x]
        )

    with col2:
        año = st.number_input(
            "Año",
            min_value=2020,
            max_value=2030,
            value=date.today().year
        )

    cal = calendar.monthcalendar(año,mes)
    st.subheader(f"{calendar.month_name[mes]} { año}")
    dias_semana = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
    cols = st.columns(7)

    for i, dia in enumerate(dias_semana):
        cols[i].markdown(f"**{dia}**")

    for semana in cal:
        cols = st.columns(7)
        for i, dia in enumerate(semana):
            if dia == 0:
                cols[i].write("")
            else: 
                fecha_str = f"{año}-{mes:02d}-{dia:02d}"
                
                if fecha_str in st.session_state.turnos:
                    turno = st.session_state.turnos[fecha_str]
                    texto = f"{dia}\n {turno['inicio']} - {turno['fin']}"
                else:
                    texto = f"{dia}\n-"
                
                if cols[i].button(texto, key=fecha_str):
                    st.session_state["dia_seleccionado"]=fecha_str

    #Se formula el turno

    if "dia_seleccionado" in st.session_state:
        fecha = st.session_state["dia_seleccionado"]
        st.subheader(f"Registrar turno para: {fecha}")

        hora_inicio = st.time_input("Hora inicio", time(8,0))
        hora_fin = st.time_input("Hora fin", time(17,0))
        horas_extra = st.number_input(
            "Horas extra registradas",
            min_value=0,
            max_value=12,
            value=0,
            step=1
        )

        if st.button("Guardar turno"):  
            st.session_state.turnos[fecha] = {
                    "inicio":hora_inicio,
                    "fin":hora_fin,
                    "extra": horas_extra
                }
            st.success("Turno guardado correctamente" )
            #st.json(st.session_state.turnos)