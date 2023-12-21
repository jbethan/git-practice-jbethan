import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title=None, layout="wide")

st.header("Recently Graduated Data Professional Seeks Affordable Life")
st.markdown('These data visualizations provide an exploratory of the affordability of each state to a recently graduated data professional. They focus on income and job availability, housing costs (rent and owned), and tax burden')

st.markdown('Use the interactive graphs below to explore data by state.')
# %%
data = pd.read_csv('https://raw.githubusercontent.com/jbethan/finalproj_state_affordability/main/2023_state_dataset.csv', index_col=None)
data = data.drop(data.columns[0], axis=1)
data.head()

# %%
data = data.rename(columns={"Annual Average Wage" : "All Industry Average Salary"})
data['Total Tax Burden'] = data['Total Tax Burden']/100
data['Property Tax Burden'] = data['Property Tax Burden']/100 
data['Income Tax Burden'] = data['Income Tax Burden']/100
data['Sales Tax Burden'] = data['Sales Tax Burden']/100

# %%
# GROUP 1 PLOT INCOME METRICS

# Graphs
# Salary Comparison by State for Data Analysts
st.header('Income Metrics')

st.subheader('Income Data by State')
option1 = st.selectbox(
    'Select a State:',
    ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado','Connecticut','Delaware','Florida','Georgia',
     'Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
     'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York',
     'North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
     'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'
), key='option')

income_data = data.loc[data['State']==option1, ['State','Data Analyst Average Salary', 'Data Analyst Job Count as of 09/14/23', 'Data Scientist Average Salary', 'Data Scientist Job Count as of 09/14/23']]
income_data.reset_index(drop=True)
st.table(income_data)

salary_type_data = pd.melt(data, id_vars=['State'], value_vars=['All Industry Average Salary','Data Analyst Average Salary', 'Data Scientist Average Salary'], 
                         var_name="Salary Group", value_name='Average Salary')
salary_type_data['Salary Group'] = salary_type_data['Salary Group'].str.replace('Average Salary', '')
salary_type_data.head()

# %%

# Average Salary by Job Type
fig3 = px.violin(salary_type_data, 
                 y="Average Salary", 
                 x="Salary Group",
                 color = "Salary Group",
                 color_discrete_sequence= ["#5d8b7c", "#8fb5c9", "#91c0be"],
                 points="all",
                 hover_name = salary_type_data['State'],
                 title = 'Average Salary Distribution by Job Type Across All States'
                 )

fig3.update_layout(height=600,
                   width=1200, 
                   plot_bgcolor="#F2EBDF"
                   )
st.plotly_chart(fig3)

st.markdown('Compare distribution of salary averages by job type. Hover for individual state data. Notice that just because state has a high associated cost of living doesn\'t mean they have the highest average salary.')
