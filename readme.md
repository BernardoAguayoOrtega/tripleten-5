# Análisis Exploratorio de Datos de EPL Soccer

Este proyecto realiza un análisis exploratorio de datos de jugadores de la Premier League Inglesa (EPL) utilizando diversas tecnologías como Python, pandas, plotly, y Streamlit.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación utilizado para procesar y analizar datos.
- **pandas:** Biblioteca para la manipulación y análisis de datos.
- **plotly:** Biblioteca de gráficos interactivos para visualización de datos.
- **Streamlit:** Framework para crear aplicaciones web interactivas y compartir visualizaciones de datos.

## Estructura del Proyecto

├── data/
│ └── EPL_Soccer.csv
├── .streamlit/
│ └── config.toml
├── notebooks/
│ ├── EDA.ipynb
├── app.py
├── init_project.py
└── requirements.txt


- `data/EPL_Soccer.csv`: Archivo CSV con los datos de jugadores.
- `streamlit/config.toml`: Archivo de configuración para Streamlit.
- `app.py`: Script principal para ejecutar la aplicación Streamlit.
- `requirements.txt`: Archivo con las dependencias necesarias para el proyecto.

## Configuración de Streamlit

Para hacer que tu aplicación Streamlit sea compatible con Render, se añadió un archivo de configuración `config.toml` en la carpeta `streamlit`:

```toml
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
```

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/BernardoAguayoOrtega/tripleten-5
   cd tripleten-5
    ```

2. **Ejecutar init project file:**
    ```bash
    python init_project.py
     ```

## Ejecución Local

Para ejecutar la aplicación Streamlit localmente, usa el siguiente comando:

```bash
streamlit run app.py
```
## Despliegue en Render

1. **Crea el repositorio en GitHub:**

   Asegúrate de que todos los archivos necesarios estén comprometidos en tu repositorio de GitHub.

2. **Configura Render:**

   - Ve a [Render.com](https://render.com) y crea una nueva cuenta o inicia sesión.
   - Crea un nuevo servicio web y conecta tu repositorio de GitHub.
   - Configura los parámetros del servicio para que coincidan con tu archivo `config.toml`.
   - Establece el comando de ejecución como `streamlit run your_script.py`.

## Funcionalidades de la Aplicación

La aplicación incluye varias funcionalidades para analizar y visualizar los datos de jugadores de la EPL:

- **Histograma del Ratio de Minutos por Gol:** Proporciona una visión de cómo se distribuye el ratio de minutos por gol entre los jugadores.
- **Gráfico de Dispersión de Goles vs. Distancia Recorrida:** Visualiza la relación entre la distancia recorrida y la cantidad de goles, utilizando el tamaño de los puntos para representar los tiros por juego y el color para los clubes.
- **Boxplot del Score por Club:** Muestra la distribución del score de los jugadores en diferentes clubes, permitiendo identificar posibles outliers y comparaciones entre equipos.
- **Gráfico de Barras de IMC por Club:** Compara el Índice de Masa Corporal (IMC) de los jugadores entre diferentes clubes.


## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerencias y mejoras.
