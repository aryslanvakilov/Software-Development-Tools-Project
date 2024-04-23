import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

st.header('Market for used cars')
st.write("""
         ##### Filter the data below to see the ads by manufacturer""")
show_new_cars = st.checkbox('Include new cars from dealers')
if not show_new_cars:
    df = df[df.condition!='good']


manufacturer_choice = df['model'].unique()
users_choice = st.selectbox('Select model:', manufacturer_choice)

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())


df_filtered = df[df.model == users_choice]

year_range = st.slider("Choose years",
                       value=(min_year, max_year),min_value=min_year,max_value=max_year)

show_records = st.number_input("Numbers of records to show", min_value=5, max_value=len(df_filtered))
                       
actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df[(df.model==users_choice) & (df.model_year >= year_range[0]) & (df.model_year <= year_range[1])]
st.table(df_filtered[:show_records])

st.header('Price analysis')
st.write("""###### Let's analyze what price influences the most. We'll check how distribution of price varies depending on 
transmission,cylinders,fuel and type""")

list_for_hist = ['transmission','cylinders','fuel','type']
selected_type = st.selectbox('Split for price distribution', list_for_hist)

fig1 = px.histogram(df, x='price', labels={"price": "Price"}, color=selected_type)
fig1.update_layout(
    title="<b> Split of price by {}</b>".format(selected_type),
    yaxis_title="Number of records"
    )

st.plotly_chart(fig1)
fig1.show()



list_for_scatter = ['odometer','paint_color','is_4wd']
choice_for_scatter = st.selectbox('Price dependency on',list_for_scatter)
fig2 = px.scatter(df, x='price', y=choice_for_scatter, hover_data=['model_year'])

fig2.update_layout(title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)
fig2.show()