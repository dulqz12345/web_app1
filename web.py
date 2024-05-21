import streamlit as st
import functions

countries = functions.get_countries()


def add_country():
    country = st.session_state["new_country"] + "\n"
    countries.append(country)
    functions.write_countries(countries)


st.title("My Countries App")
st.subheader("This is my countries app.")
st.write("This app is to increase tour knowledge about the world.")

for index, country in enumerate(countries):
    checkbox = st.checkbox(country, key=country)
    if checkbox:
        countries.pop(index)
        functions.write_countries(countries)
        del st.session_state[country]
        st.rerun()

st.text_input(label="Country", placeholder="Enter a country...", label_visibility="hidden",
              on_change=add_country, key="new_country")

