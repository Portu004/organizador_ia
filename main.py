import streamlit as st
import pandas as pd
from tareas import agregar_tarea, marcar_completada, eliminar_tarea
from utils import cargar_tareas
from ia import sugerir_prioridad, detectar_similares
from visualizacion import grafico_tareas_por_categoria, grafico_tareas_por_fecha

st.title("Organizador Inteligente de Tareas")

# Cargar datos
df = cargar_tareas()

# Mostrar tareas
st.subheader("Tareas actuales")
st.dataframe(df)

# Agregar nueva tarea
st.subheader("Agregar nueva tarea")
with st.form("nueva_tarea"):
    descripcion = st.text_input("Descripción")
    categoria = st.text_input("Categoría")
    fecha_limite = st.date_input("Fecha límite")
    duracion = st.number_input("Duración estimada (horas)", min_value=1, max_value=24)
    submitted = st.form_submit_button("Agregar")
    if submitted:
        agregar_tarea(descripcion, categoria, fecha_limite, duracion)
        st.success("Tarea agregada. Recarga la página para ver los cambios.")

# Marcar como completada
st.subheader("Marcar tarea como completada")
tarea_id = st.number_input("ID de la tarea", min_value=1, step=1)
if st.button("Marcar completada"):
    marcar_completada(tarea_id)
    st.success("Tarea marcada como completada. Recarga la página.")

# Eliminar tarea
st.subheader("Eliminar tarea")
tarea_id_del = st.number_input("ID a eliminar", min_value=1, step=1, key='del')
if st.button("Eliminar tarea"):
    eliminar_tarea(tarea_id_del)
    st.success("Tarea eliminada. Recarga la página.")

# Sugerencias inteligentes
st.subheader("Sugerencias inteligentes")
prioridad = sugerir_prioridad(df)
st.write("Orden sugerido de prioridades:")
st.dataframe(prioridad)

similares = detectar_similares(df)
if similares:
    st.write("Tareas similares detectadas:")
    for grupo in similares:
        st.write(", ".join(grupo))
else:
    st.write("No se detectaron tareas similares.")

# Visualización
st.subheader("Visualización")
st.plotly_chart(grafico_tareas_por_categoria(df))
st.plotly_chart(grafico_tareas_por_fecha(df))
