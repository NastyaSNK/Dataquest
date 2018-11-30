#!/usr/bin/env python
# coding: utf-8

# ## CIA World Factbook Analysis

# <li>population - The population as of 2015.<p>
# <li>population_growth - The annual population growth rate, as a percentage.<p>
# <li>area - The total land and water area.<p>
# <li>name - The name of the country.<p>
# <li>area - The total land and sea area of the country.<p>
# <li>population - The country's population.<p>
# <li>population_growth- The country's population growth as a percentage.<p>
# <li>birth_rate - The country's birth rate, or the number of births a year per 1,000 people.<p>
# <li>death_rate - The country's death rate, or the number of death a year per 1,000 people.<p>
# <li>area- The country's total area (both land and water).<p>
# <li>area_land - The country's land area in square kilometers.<p>
# <li>area_water - The country's waterarea in square kilometers.<p>

# connect to a SQLite database and query it using the sqlite3 module.
# 1st variant with tuples in result

# In[2]:


import sqlite3
import pandas as pd
conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
q1 = "SELECT * FROM facts;"
cursor.execute(q1).fetchall()


# 2nd variant - read the result in pandas dataframe

# In[3]:


conn = sqlite3.connect("factbook.db")
q = "SELECT * FROM facts;"
res1=pd.read_sql_query(q, conn)
q5="SELECT * FROM facts LIMIT 5;"
res2=pd.read_sql_query(q5, conn)


# In[4]:


res2


# # Single query that returns the: min&max population, population growth

# In[5]:



q3 = "SELECT MIN(population),MAX(population), MIN(population_growth), MAX(population_growth) FROM facts;"
res3=pd.read_sql_query(q3, conn)


# In[6]:


res3


# ## Single query that returns the: min&max population, population growth

# In[7]:


q4 = "SELECT * FROM facts where population =(SELECT MIN(population) FROM facts) ;"
res4=pd.read_sql_query(q4, conn)


# In[8]:


res4


# In[9]:


q5 = "SELECT * FROM facts where population =(SELECT MAX(population) FROM facts) ;"
res5=pd.read_sql_query(q5, conn)


# In[10]:


res5


# This cell contains country name:world & antarctica. Word with anomalously large value and Antarctica with zero number of population

# In[11]:


q6 = "SELECT * FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) ;"
res6=pd.read_sql_query(q6, conn)
res6


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[13]:


plt.hist(res6["population"])


# In[21]:


q7 = "SELECT population,population_growth,birth_rate,death_rate  FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) ;"
res7=pd.read_sql_query(q7, conn)
fig = plt.figure(figsize=(12, 5))
ax1=fig.add_subplot(1,4,1)
res7.hist(ax=ax1)
plt.show()


# ### Which countries have the highest population density?

# In[37]:


q8 = "SELECT cast (population as float)/cast (area_land as float) density, name  FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) ORDER BY density DESC LIMIT 10;"
res8=pd.read_sql_query(q8, conn)
res8


# #### Histogram of population densities

# In[39]:


q9 = "SELECT cast (population as float)/cast (area_land as float) density  FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) ORDER BY density DESC;"
res9=pd.read_sql_query(q8, conn)
fig = plt.figure(figsize=(12, 5))
ax1=fig.add_subplot(1,1,1)
res8.hist(ax=ax1)
plt.show()


# In[41]:


q10 = "SELECT cast(area_water as float)/cast(area_land as float) density  FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) ORDER BY density DESC LIMIT 10;"
res10=pd.read_sql_query(q10, conn)
res10


# In[43]:


q10 = "SELECT area_water/area_land density  FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) ORDER BY density DESC;"
res10=pd.read_sql_query(q10, conn)
fig = plt.figure(figsize=(12, 5))
ax1=fig.add_subplot(1,1,1)
res10.hist(ax=ax1)
plt.show()


# ### Which countries have more water than land?

# In[45]:


q10 = "SELECT name,cast(area_water as float)/cast(area_land as float) density  FROM facts where population !=(SELECT MAX(population) FROM facts) and population !=(SELECT MIN(population) FROM facts) and area_water>area_land ORDER BY density DESC LIMIT 10;"
res10=pd.read_sql_query(q10, conn)
res10


# Virgin Islad is a country wich have more water than land
