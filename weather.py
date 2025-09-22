import altair as alt
import polars as pl
import streamlit as st
import wikipedia
from streamlit_searchbox import st_searchbox

df = pl.DataFrame({
    'city': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'month': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'precip': [2.68, 0.87, 5.31, 3.94, 4.13, 3.58, 3.62, 3.98, 2.56]
})

chart = alt.Chart(df).mark_bar().encode(
    x = "city",
    y = "average(precip)"
)



def search_wikipedia(searchterm: str) -> list:
    # search wikipedia for the searchterm
    return wikipedia.search(searchterm) if searchterm else []


# pass search function and other options as needed
selected_value = st_searchbox(
    search_wikipedia,
    placeholder="Search Wikipedia... ",
    key="my_key",
)


st.header("Weather")
st.altair_chart(chart)
st.write(f"Selected value: {selected_value}")