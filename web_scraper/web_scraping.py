# -*- coding: utf-8 -*-
"""Web Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oYAKmWoKkWYt4R5ZdGNtHs3E9OMKBoxz

<h1>Assignment 3 - Web Scraping</h1>

**In this assignment you need to work with data from the [worldometers](https://www.worldometers.info/coronavirus/) website. I want you to scrape all 215 countries information about coronavirus cases from the website.**
The data has to include:
- `Country name`
- `Total cases`
- `Total deaths`
- `Total recovered`
- `Active cases`
- `New cases`
- `New deaths`
- `Total tests`
- `Population`

**You need to use beautiful soup 4 and regular expressions for this task. Save results in csv file and read this dataset**

<h3> Import Dependencies
</h3>
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

"""<h3> Starting scrape the data </h3>

"""

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('table')
    rows = table.find_all('tr')
    list_rows = []

    for row in rows:
        cells = row.find_all('td')
        clean_row = []

        for cell in cells:
            str_cell = str(cell)
            clean = re.compile('<.*?>')
            clean_text = re.sub(clean, '', str_cell)
            clean_text = clean_text.strip()
            clean_text = re.sub(r'\s+', ' ', clean_text)
            clean_row.append(clean_text)
        list_rows.append(clean_row)

    for clean_row in list_rows:
        clean_row

else:
    print("Failed to retrieve the webpage")

df = pd.DataFrame(list_rows)
string_to_check = '<td style="font-weight: bold; text-align:right;">'
df = df[df.apply(lambda row: row.astype(str).str.contains(string_to_check).any(), axis=1)]
df = df.iloc[:, :15]

new_value = ''
df.replace(to_replace=string_to_check, value=new_value, regex=True, inplace=True)

df.head()

col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
cleantext2 = cleantext2.strip()
cleantext2 = re.sub(r'\s+', ' ', cleantext2)
all_header.append(cleantext2)

df_header = pd.DataFrame(all_header)
df_header = df_header[0].str.split(',', expand=True)
df_header = df_header.iloc[0:1, :17]
df_header.drop(columns=[2], inplace=True)
df_header.drop(columns=[11], inplace=True)
df_header.columns = range(df_header.shape[1])

frames = [df_header, df]
data = pd.concat(frames)
data = data.rename(columns=data.iloc[0])
data.drop(data.columns[0], axis=1, inplace=True)
data.reset_index(drop=True, inplace=True)
data.columns = data.columns.str.replace(' ', '')
data.drop(data.index[0], axis=0, inplace=True)
data.head()

# Validation - USA
data[data['Country'] == 'USA']

"""<h3> Save & Read CSV
</h3>
"""

#Write File
data.to_csv('coronavirus_data.csv', index=False)

# Read file
new_df = pd.read_csv('coronavirus_data.csv')
new_df.head()