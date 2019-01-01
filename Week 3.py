#!/usr/bin/env python
# coding: utf-8

# ### Week 3 Capstone

# In[1]:


#Import Library
import requests
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np

print("Import complete!")


# ### Import Data

# In[5]:


wiki = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

source_code = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")
soup = BeautifulSoup(source_code.content, 'html.parser')
table = soup.find_all('table')       
raw_data = pd.read_html(str(table))


# In[ ]:





# In[7]:


# Transform into Dataframe

data = np.array(raw_data)
df = pd.DataFrame(data[0])

# Naming Columns
df.columns = ['Postcode', 'Borough', 'Neighbourhood']

# Remove the top row
df = df.iloc[1:]


# Remove the top row
df = df[df.Borough != 'Not assigned']
df = df[df.Neighbourhood != 'Not assigned']


# In[9]:


df.shape


# In[10]:


df

