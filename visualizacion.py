import plotly.express as px

def grafico_tareas_por_categoria(df):
    return px.histogram(df, x='categoria', color='completada', barmode='group', title='Tareas por Categoría')

def grafico_tareas_por_fecha(df):
    return px.histogram(df, x='fecha_limite', color='completada', barmode='group', title='Tareas por Fecha Límite')
