from utils import cargar_tareas, guardar_tareas
import pandas as pd

def agregar_tarea(descripcion, categoria, fecha_limite, duracion):
    df = cargar_tareas()
    nueva_id = df['id'].max() + 1 if not df.empty else 1
    nueva_tarea = {
        'id': nueva_id,
        'descripcion': descripcion,
        'categoria': categoria,
        'fecha_limite': fecha_limite,
        'duracion': duracion,
        'completada': False
    }
    df = df.append(nueva_tarea, ignore_index=True)
    guardar_tareas(df)

def marcar_completada(tarea_id):
    df = cargar_tareas()
    df.loc[df['id'] == tarea_id, 'completada'] = True
    guardar_tareas(df)

def eliminar_tarea(tarea_id):
    df = cargar_tareas()
    df = df[df['id'] != tarea_id]
    guardar_tareas(df)
