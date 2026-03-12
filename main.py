import streamlit as st
from datetime import time, datetime, timedelta
import holidays
import pandas as pd

from calendar_shift import show_calendar

st.write("Registro de horas")

show_calendar()

#fecha = st.date_input("Fecha trabajada")
festivos_colombia = holidays.Colombia()
#hora_inicio = st.time_input("Hora de inicio", time(8,0))
#hora_fin = st.time_input("Hora final", time(18,0))

#domingo = fecha.weekday() == 6


if "turnos" in st.session_state and st.session_state.turnos:
    resumen = {
        "diurnas_ordinarias" : 0,
        "nocturnas_ordinarias" : 0,
        "dominical_diurnas" : 0,
        "dominical_nocturnas" : 0,
        "festivo_diurno" : 0,
        "festivo_nocturno": 0,
        "extra_diurna" : 0,
        "extra_nocturna": 0
    }

    horas_semana = {}

    for fecha, turno in st.session_state.turnos.items():

        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")

        semana = fecha_dt.isocalendar().week
        if semana not in horas_semana:
            horas_semana[semana] = 0

        inicio = datetime.combine(fecha_dt, turno["inicio"])
        fin = datetime.combine(fecha_dt, turno["fin"])

        ### Condicion para cambio de dia durante turno de noche
        if fin <= inicio:
            fin += timedelta(days=1)
        hora_actual = inicio.replace(minute=0, second=0, microsecond=0)

        while hora_actual < fin:

            limite_nocturno = (
                hora_actual.time() >= time(19,0) or hora_actual.time() < time(6,0)
            )
            domingo = hora_actual.weekday() == 6
            festivo = hora_actual.date() in festivos_colombia

            horas_semana[semana] += 1
            calculo_extra = horas_semana[semana] > 44

            if calculo_extra:
                if limite_nocturno:
                    resumen["extra_nocturna"] += 1
                else:
                    resumen["extra_diurna"] += 1
            else:

                if festivo:
                    if limite_nocturno:
                        resumen["festivo_nocturno"] += 1
                    else:
                        resumen["festivo_diurno"] += 1
                
                elif domingo:
                    if limite_nocturno:
                        resumen["dominical_nocturnas"] += 1
                    else:
                        resumen["dominical_diurnas"] += 1
                
                else:
                    if limite_nocturno:
                        resumen["nocturnas_ordinarias"] += 1
                    else:
                        resumen["diurnas_ordinarias"] += 1

            hora_actual += timedelta(hours=1)

    st.subheader("Resumen mensual")            
    st.write(resumen)
    df = pd.DataFrame([resumen])

    st.download_button (
        "Descargar resumen",
        df.to_csv(index=False),
        "novedades_turnos.cvs,"
        "text/csv"
    )
        










