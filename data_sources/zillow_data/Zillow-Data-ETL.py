#!/usr/bin/env python
# coding: utf-8

# ## A Quick ETL (Extract - Tranform - Load) Process to Showcase Python's Pandas library
# ### Source Data: Zillow's Median Home Value with Time Series
# ### ETL process:
# #### 1- clean up data, remove unused columns, rename columns
# #### 2 - filter out data to obtain only Austin-RoundRock metro area
# #### 3 - calculate YoY value change in percentage format
# #### 4 - calculate median home value each year
# #### 5 - export data to csv for loading into database or analytical process
# #### 6 - bonus: we can build visualization here in Python to quickly see trends and projections

# In[1]:


# input dependencies
import pandas as pd
import numpy as np


# In[2]:


# original Zillow data set
inputFile = "data-source/Zip_Zhvi_SingleFamilyResidence.csv"

csv_reader = pd.read_csv(inputFile, encoding='latin-1')

df = pd.DataFrame(csv_reader)
df.rename(index=str, columns={'RegionName' : 'Zip'}, inplace = True)
df.head()


# In[3]:


# clean up unused columns
df.drop(columns=['RegionID'], inplace = True)


# In[4]:


df = df.loc[df['Metro'] == 'Austin-Round Rock']
df.head()


# In[5]:


def avgHomeValue (list):
    return round(sum(list)/len(list),2)

df1 = pd.DataFrame()

df1['Zip'] = df['Zip']
df1['City'] = df['City']
df1['County'] = df['CountyName']

# calculate yearly average of home value
monthList = []
for i in range (1997, 2019):
    for j in range (1,13):
        if j<10:
            monthList.append(df[str(i) + '-0' + str(j)])
        else:
            monthList.append(df[str(i) + '-' + str(j)])
        j += 1
    df1[str(i)] = avgHomeValue(monthList)

# reset index
df1 = df1.reset_index(drop=True)
df1.head()


# In[6]:


# function calculating year over year value change in percentage, level of detail to 1 digit after dicimal point
def pctChange (x, y):
    return round((x-y)/y*100, 1)

df2 = pd.DataFrame()

df2['Zip'] = df['Zip']
df2['City'] = df['City']
df2['County'] = df['CountyName']

# calculating each year's percentage of change
for i in range(1996, 2018):
    j = i+1
    currentMon = str(j) + '-12'
    lastMon = str(i) + '-12' 
    df2[str(j)] = pctChange(df[currentMon], df[lastMon])
    i += 1

# reset index
df2 = df2.reset_index(drop=True)
df2.head()


# In[7]:


# export result to output csv file
output1 = 'zillow-median-home-value-YoY.csv'
output2 = 'zillow-yoy-price-change-Percent.csv'
df1.to_csv(output1, index=True)
df2.to_csv(output2, index=True)


# In[8]:


# still a working progress, further data transformation is needed.

import matplotlib.pyplot as plt

df2 = df1.T

df2.reset_index()

xlim = df2.iloc[:,1]
xlim = list(xlim)
xlim = xlim[3:]
xlim


# In[9]:


ylim = df2.index.values
ylim = list(ylim[3:])
ylim

plt.plot(ylim, xlim)
plt.xticks(rotation='vertical')
plt.show()


# In[10]:


get_ipython().system('jupyter nbconvert --to Python Zillow-Data-ETL.ipynb')

