import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
data = pd.read_csv('data/EPL_Soccer.csv')

# Crear un encabezado
st.header('Análisis Exploratorio de Datos de EPL Soccer')

# Crear un botón para construir un histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para el conjunto de datos de EPL Soccer')
    fig = px.histogram(data, x="MinutestoGoalRatio", title="Histograma del Ratio de Minutos por Gol")
    st.plotly_chart(fig, use_container_width=True)

# Crear un gráfico de dispersión de Goals vs. DistanceCovered
if st.button('Mostrar Gráfico de Dispersión'):
    st.write('Gráfico de Dispersión de Goles vs. Distancia Recorrida')
    fig = px.scatter(data, x="DistanceCovered(InKms)", y="Goals", 
                     size="ShotsPerGame", color="Club", hover_name="PlayerName",
                     title="Goles vs. Distancia Recorrida (con Tiros por Juego como tamaño del marcador)")
    st.plotly_chart(fig, use_container_width=True)

# Crear un boxplot del Score por Club
if st.button('Mostrar Boxplot'):
    st.write('Boxplot del Score por Club')
    fig = px.box(data, x="Club", y="Score", title="Distribución del Score por Club")
    st.plotly_chart(fig, use_container_width=True)

# Crear un gráfico de barras de BMI por Club
if st.button('Mostrar Gráfico de Barras'):
    st.write('Gráfico de Barras de IMC por Club')
    fig = px.bar(data, x="Club", y="BMI", color="PlayerName", title="IMC por Club")
    st.plotly_chart(fig, use_container_width=True)
