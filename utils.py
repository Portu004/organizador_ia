import pandas as pd

DATA_PATH = 'data/tareas.csv'

def cargar_tareas():
    return pd.read_csv(DATA_PATH)

def guardar_tareas(df):
    df.to_csv(DATA_PATH, index=False)
