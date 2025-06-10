import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def sugerir_prioridad(df):
    # Sugerir tareas no completadas, ordenadas por fecha límite y duración
    pendientes = df[df['completada'] == False]
    return pendientes.sort_values(['fecha_limite', 'duracion'])

def detectar_similares(df):
    # Detecta tareas similares por descripción
    pendientes = df[df['completada'] == False]
    if pendientes.shape[0] < 2:
        return []
    textos = pendientes['descripcion'].tolist()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)
    n_clusters = min(3, len(textos))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    clusters = kmeans.fit_predict(X)
    similares = {}
    for idx, cluster in enumerate(clusters):
        similares.setdefault(cluster, []).append(pendientes.iloc[idx]['descripcion'])
    # Solo mostrar grupos con más de una tarea
    return [v for v in similares.values() if len(v) > 1]
