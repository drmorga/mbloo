#!/usr/bin/env python
# coding: utf-8

# 
# # Worldwide Coffee Habits Analysis
# 
# Explore trends in coffee consumption, pricing, and preferences across various fictional countries using synthetic data.
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set plot styles
sns.set(style="whitegrid")


# In[4]:


# Load the dataset
df = pd.read_csv("worldwide_coffee_habits.csv")

# Preview
df.head(20)


# In[5]:


# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Check for nulls
df.isnull().sum()


# In[6]:


# Summary statistics
df.describe()

# Unique coffee types
df['type_of_coffee_consumed'].value_counts()


# In[7]:


plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='year', y='coffee_consumption_(kg_per_capita_per_year)', ci=None)
plt.title("Global Average Coffee Consumption Over Time")
plt.ylabel("kg per capita per year")
plt.xlabel("Year")
plt.tight_layout()
plt.show()


# In[9]:


plt.figure(figsize=(10,5))
df['type_of_coffee_consumed'].value_counts().plot(kind='bar', color='blue')
plt.title("Most Popular Types of Coffee")
plt.ylabel("Number of Entries")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[10]:


plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Between Numeric Variables")
plt.tight_layout()
plt.show()


# In[11]:


top_consumers = df.groupby('country')['coffee_consumption_(kg_per_capita_per_year)'].mean().sort_values(ascending=False).head(10)
top_consumers.plot(kind='barh', color='saddlebrown', title='Top 10 Countries by Avg Coffee Consumption')
plt.xlabel("Avg kg per capita per year")
plt.tight_layout()
plt.show()


# In[14]:


top_consumers = df.groupby('country')['coffee_consumption_(kg_per_capita_per_year)'].mean().sort_values(ascending=False).head(10)
top_consumers.plot(kind='pie', title='Top 10 Countries by Avg Coffee Consumption')
plt.xlabel("Avg kg per capita per year")
plt.tight_layout()
plt.show()


# 
# ## Summary
# 
# - Synthetic data gives us valuable practice for analyzing multi-variable consumption trends.
# - Americano, Mocha, and Latte appear frequently.
# - Price and consumption vary slightly across fictional countries and years.
# - This structure can be reused for real-world datasets later.
# 
# 
