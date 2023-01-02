import streamlit as st
import pandas as pd
import plotly.express as px

from pybadges import badge

# Config default settings of the page
st.set_page_config(
    page_title="Temas Populares en GitHub",
    page_icon="assets/github-mark.png",
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)


@st.cache
def load_data():
    return pd.read_csv(
        filepath_or_buffer='data/repos.csv',
        sep=',',
        header=0,
        encoding='utf-8',
        engine='python')


st.title('Temas Populares en GitHub')

st.image('assets/github-mark.png')

st.header('Los lenguajes de programacion con mas repos en GitHub 2022⭐')

df = load_data()

# descripcion de la aplicacion
st.markdown('''
    Esta aplicacion muestra los lenguajes de programacion con mas repositorios en GitHub.

    Existen *453* lenguajes de programacion con repositorios en GitHub, una de las
    plataformas mas grandes de codigo abierto.

    Los registros abarcan los años a partir del 2011 hasta el 2022.
    ''')

st.subheader('Lenguajes con mas repositorios')

# muestra los primeros 10 lenguajes de programacion
st.table(df.head(10))

st.markdown('''Entre los lenguajes de programacion con mas repositorios en 
GitHub se encuentraan los lenguajes enfocados al desarrollo web, como JavaScript,
CSS, HTML, entre los primeros 3 puestos seguido de shell y Python.''')

st.subheader('Lenguajes con menos repositorios')

st.table(df.tail(10))

st.markdown('''Los lenguajes con menor cantuidad de repositorios en GitHub 
llegan a tener solo un registro, algunos de estos caen en la categoria de 
herramientas y no tanto como lenguajes de programacion en plena forma.''')

st.subheader('Graficas')

top = df.head(25)

st.plotly_chart(px.bar(top, x='languaje', y='repos'))
st.plotly_chart(px.pie(top, values='repos', names='languaje'))
