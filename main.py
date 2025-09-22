import streamlit as st


weather = st.Page("weather.py", title="Weather", icon=":material/add_circle:")
penguins = st.Page("burtin.py", title="Penguin", icon=":material/add_circle:")

pg = st.navigation([weather,penguins])
st.set_page_config(
    page_title="Prueba",
    page_icon="𝚾",
    initial_sidebar_state="expanded"
)

pg.run()