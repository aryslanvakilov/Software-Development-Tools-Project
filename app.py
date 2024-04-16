import streamlit as st
import pandas as pd

st.title("Hello")

df = pd.read_csv('vehicles_us.csv')

st.write(df.head())
st.header('Market for used cars')
st.write("""##### Filtering data below to see the add by model""")
show_new_cars = st.checkbox('Include new cars from deakers')


if not show_new_cars:
    df = df[df.condition!='good']

# creating options for filter for all manufacturers 
manufacturer_choice = df['model'].unique()
users_choice = st.selectbox('Select model:', manufacturer_choice)