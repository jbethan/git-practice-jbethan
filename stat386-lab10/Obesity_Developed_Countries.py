# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# %%
wiki1 = 'https://en.wikipedia.org/wiki/Developed_country#Comparative_table_(2023)'
response = requests.get(wiki1)
print(response.status_code)

#df.head()
# %%
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all("table",{"class":"wikitable mw-collapsible"})

# %%
df = pd.read_html(str(table))
# convert list to dataframe
df = pd.DataFrame(df[0])

# %%
df.columns = df.columns.get_level_values(1)
df.columns.to_flat_index()
df = df.drop(columns = ["HDI[31]", "IMF[32]", "WB[24]", "Per capita PPP 2023[33]"], axis=1)

# %%
df = df[~df.Countries.str.contains(r"\d{4}")]
df = df.reset_index(drop=True)

# %%
end = int(df[df["Countries"] == "Switzerland"].index.values)
df = df[0:end+1]

# %%
wiki2 = 'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate'
response = requests.get(wiki2)
print(response.status_code)

# %%
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all("table",{"class":"wikitable"})

# %%
df2 = pd.read_html(str(table))
# convert list to dataframe
df2 = pd.DataFrame(df2[0])
df2 = df2.rename(columns={"Country": "Countries"})
df2.head()

# %%
df = df.merge(df2, how='left', on='Countries')

# %%
df = df.sort_values(by=["Obesity rate (%)"], ascending=False)
df = df.reset_index(drop=True)
# %%
df

# %%
df2[df2["Countries"]== "China"]
# %%
df2[df2["Obesity rate (%)"] < 10]
# %%
df2
# %%
df2.to_csv('2023_obesity_by_country.csv')
# %%
