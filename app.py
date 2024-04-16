import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.write(df.head())
st.header('Market for used cars')
show_new_cars = st.checkbox('Include new cars from deakers')
show_new_cars

if not show_new_cars:
    df = df[df.condition!='good']

# creating options for filter for all manufacturers 
manufacturer_choice = df['model'].unique()
users_choice = st.selectbox('Select model:', manufacturer_choice)
manufacturer_choice
users_choice

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())
year_range = st.slider("Choose years",
                       value=(min_year, max_year),min_value=min_year,max_value=max_year)
year_range

filtered_type = df[(df.model==users_choice) & (df.model_year >= year_range[0]) & (df.model_year <= year_range[1])]
st.table(filtered_type)

st.header('Price analysis')
list_for_hist = ['transmission','cylinders','fuel','type']
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)
fig1 = px.histogram(df, x='price', color=choice_for_hist)

#adding title
fig1.update_layout(title="<b> Split of price by {}</b>".format(choice_for_hist))
#into streamlit
st.plotly_chart(fig1)
fig1.show()

list_for_scatter = ['odometer','paint_color','is_4wd']
choice_for_scatter = st.selectbox('Price dependency on',list_for_scatter)
fig2 = px.scatter(df, x='price', y=choice_for_scatter, hover_data=['model_year'])

fig2.update_layout(title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)
fig2.show()