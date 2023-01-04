import streamlit as st
import pandas as pd
import plotly.express as px

from pybadges import badge

# Config default settings of the page
st.set_page_config(
    page_title="Lenguajes de programacion mas Populares en GitHub",
    page_icon="assets/github-mark.png",
    layout='centered',
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


st.title('Lenguajes de programacion mas populares en GitHub')

column1, column2, column3 = st.columns(3)

with column2:
    st.image('assets/github-mark.png')

st.header('Los lenguajes de programacion con mas repositorios en GitHub 2022⭐')

df = load_data()

st.markdown('''
    Esta aplicacion muestra los lenguajes de programacion con mas repositorios en GitHub.

    Existen *453* lenguajes de programacion con repositorios en GitHub, una de las
    plataformas mas grandes de codigo abierto.

    Los registros abarcan los años a partir del 2011 hasta el 2022.
    ''')

st.subheader('Lenguajes con mas repositorios')

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

st.markdown('''
    [![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joelbuenrostro/)
    [![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/esteGeek)
    [![Follow](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/joel_buenrostro/)
    [![Follow](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/JoelBuenrostro/)
''')
