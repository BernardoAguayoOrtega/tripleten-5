import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
data = pd.read_csv('data/EPL_Soccer.csv')

# Crear un encabezado
st.header('Análisis Exploratorio de Datos de EPL Soccer')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de EPL Soccer')
    
    # Crear un histograma
    fig = px.histogram(data, x="MinutestoGoalRatio")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
