# %%
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# %%
df = pd.read_csv('2023_obesity_by_country.csv', index_col=None)
df = df.drop(df.columns[0], axis=1)
df.head()

#%%
iso_df = pd.read_csv('iso_alpha3_codes.csv', index_col=None)
iso_df.head()
df = df.merge(iso_df, how = "left", on=['Country Name'])


# %%
fig1 = px.choropleth(df, 
                    locations='Country Name',
                    locationmode="country names", 
                    scope='world',
                    color='Obesity rate (%)',
                    title='Obesity Rate by Country',
                    color_continuous_scale="Teal",       
                    hover_name = 'Country Name',
                    hover_data = ['Obesity rate (%)']
                    )

fig1.show()
# %%
df.head()
# %%
