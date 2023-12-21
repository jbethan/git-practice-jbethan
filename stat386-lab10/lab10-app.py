import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title=None, layout="wide")

st.header("Obesity Rate Among Developed Countries")
st.markdown('Use the interactive graphs below to explore data by country.')
# %%
df = pd.read_csv('https://raw.githubusercontent.com/jbethan/git-practice-jbethan/master/stat386-lab10/2023_obesity_by_country.csv', index_col=None)
df = df.drop(df.columns[0], axis=1)
df.head()

# %%
iso_df = pd.read_csv('https://raw.githubusercontent.com/jbethan/git-practice-jbethan/master/stat386-lab10/iso_alpha3_codes.csv', index_col=None)
iso_df.head()
df = df.merge(iso_df, how = "left", on=['Country Name'])

# %%
st.subheader("Compare Obesity Rate for Specific Countries")
option = st.multiselect('Select Countries', pd.Series(df.iloc[:,0]))
country_data = df.loc[df['Country Name'].isin(option), ['Country Name','Obesity rate (%)']]
st.table(country_data)


# %%
col1, col2 = st.columns([1, 3])

col1.header("")
col1.subheader("")
col1.subheader("")

view = col1.radio(
    "Select View",
    ["World", "Africa", "Asia", "Europe", "North America", "South America"])


if view == "Africa": 
    fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='africa',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="turbo",
                    range_color = [-10,50],       
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )
    fig1.update_layout(width=800)

elif view == "Asia":
    fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='asia',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="turbo",  
                    range_color = [-10,50],       
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )
    fig1.update_layout(width=800)

elif view == "Europe": 
    fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='europe',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="turbo", 
                    range_color = [-10,50],                            
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )
    fig1.update_layout(width=800)

elif view == 'North America':
    fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='north america',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="turbo",
                    range_color = [-10,50],       
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )
    fig1.update_layout(width=800)

elif view == "South America": 
    fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='south america',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="turbo",
                    range_color = [-10,50],       
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )
    fig1.update_layout(width=800)

else:
    fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='world',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="turbo", 
                    range_color = [-10,50],      
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )
    fig1.update_layout(width=800)

col2.plotly_chart(fig1)
# %%
