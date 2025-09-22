import altair as alt
import streamlit as st
import vega_datasets
import polars as pl

@st.cache_data
def load_data():
    return vega_datasets.data.burtin()

burtin = load_data()

st.header("Burtin")

if st.checkbox("Show raw data"):

    st.write(burtin.head())

mpg = alt.Chart(burtin).mark_line(point=True).encode(
    alt.Y('Bacteria'),
    alt.X('Genus')
)

Hj = alt.Chart(burtin).mark_line(point=True).encode(
    alt.Y('Bacteria'),
    alt.X('Penicillin')
)

chart = mpg | Hj

st.altair_chart(chart)
