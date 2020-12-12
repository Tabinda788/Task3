# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:21:09 2020

@author: DELL
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Reading Data
df=pd.read_csv("SampleSuperstore.csv")
df.head()
df.describe().T
df.info()
df.columns
print(df['Ship Mode'].unique())
print(df['Segment'].unique())
print(df['Country'].unique())
print(df['Region'].unique())
print(df['Category'].unique())
print(df['Sub-Category'].unique())
print(df['Quantity'].unique())
print(df['Discount'].unique())
col=['Country','Postal Code']
df=df.drop(columns=col,axis=1)
df.info()
df.duplicated().sum()
df.drop_duplicates(keep='first',inplace=True)
df.shape
df.isnull().sum()

s=df.groupby(['Ship Mode'],as_index=False)['Profit'].sum()
s
sns.barplot(s['Ship Mode'],s['Profit'])

s1=df.groupby(['Segment'],as_index=False)['Profit'].sum()
s1
sns.barplot(s1['Segment'],s1['Profit'])

s2=df.groupby(['Region'],as_index=False)['Profit'].sum()
s2
sns.barplot(s2['Region'],s2['Profit'])

s3=df.groupby(['Category'],as_index=False)['Profit'].sum()
s3
sns.barplot(s3['Category'],s3['Profit'])

s4=df.groupby(['Discount'],as_index=False)['Profit'].sum()
s4
sns.barplot(s4['Discount'],s4['Profit'])

s5=df.groupby(['Category'],as_index=False).sum()
s5
sns.barplot(s5['Category'],s5['Quantity'])

plt.figure(figsize=(6,6))
df['Ship Mode'].value_counts().plot(kind='pie',autopct='%1.1f%%')

plt.figure(figsize=(6,6))
df['Segment'].value_counts().plot(kind='pie',autopct='%1.1f%%')

plt.figure(figsize=(6,6))
df['Category'].value_counts().plot(kind='pie',autopct='%1.1f%%')

plt.figure(figsize=(10,10))
df['Sub-Category'].value_counts().plot(kind='pie',autopct='%1.1f%%')

df.corr()
plt.figure(figsize=(16,10))
sns.heatmap(df.corr(), annot=True, annot_kws={"size" : 14})
sns.set_style('white')
plt.xticks(fontsize=10)
plt.yticks(fontsize=14)
plt.show()

# Visualising the distribution of Sales
plt.figure(figsize=(10,10))
sns.distplot(df['Sales'],kde=True,color='g',bins=100)
sns.set()

sns.countplot(x=df['Sub-Category'])
plt.xticks(rotation=60)
plt.show()

plt.figure(figsize=(15,16))
sns.countplot(x=df['State'])
plt.xticks(rotation=90)
plt.show()

city=df['City'].value_counts()
city.plot(kind='line',figsize=(12,6))
plt.title("City Order")
plt.ylabel('Count')
plt.xlabel('City')
plt.show()

state = df.groupby(['State','City']).size()
state
state = df.groupby(['State','City']).size().reset_index(name='No of orders')
state.head()

state.plot(kind='line',figsize=(12,6))
plt.title("State and city Order")
plt.ylabel('Count')
plt.xlabel('City')
plt.show()

sns.pairplot(df,plot_kws=dict(alpha=.3, edgecolor='none'), height=2, aspect=1.1);













