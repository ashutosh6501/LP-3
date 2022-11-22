# -*- coding: utf-8 -*-
"""ML-6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oe_lVmIYZW7tV9TL7781QsT4ldcfUHXi

Sonal Shitole BC56

K-MEANS

reference : https://www.kaggle.com/code/maguser/clusters
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/drive/MyDrive/LP-3/ML/6/sales_data_sample.csv" ,encoding='unicode_escape')

df.head(5)

df.shape

df.isna().sum

df = df.drop(['ADDRESSLINE1', 'ADDRESSLINE2', 'POSTALCODE', 'CITY', 'TERRITORY', 'PHONE', 'STATE', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME', 'CUSTOMERNAME', 'ORDERNUMBER'] ,axis=1)
df.head()

df.shape   sns.barplot(x=df['Country'].value_counts())

df.isna().sum()

sns.barplot(x=df["STATUS"].value_counts().index, y=df["STATUS"].value_counts(), data=df)

"""Clusters for STATUS feature are not well distributed ,so drop this feature"""

df.drop(columns=['STATUS'], axis=1, inplace=True)

df.shape

sns.barplot(x=df["COUNTRY"].value_counts().index, y=df["COUNTRY"].value_counts(), data=df)

sns.barplot(x=df["DEALSIZE"].value_counts().index, y=df["DEALSIZE"].value_counts(), data=df)

sns.barplot(x=df["PRODUCTLINE"].value_counts().index, y=df["PRODUCTLINE"].value_counts(), data=df)

"""We have month ,year given so dropping ORDERDATE feature"""

df.drop('ORDERDATE', axis=1, inplace=True)

df.shape

df

"""Now , to apply k-means ,categorical features need to be converted into numerical .

We can do it two ways :

 1.replace()                    
 2.get_dummies()

 Replacing the values is not the most efficient way to convert them. Pandas provide a method called get_dummies which will return the dummy variable columns.

 https://www.geeksforgeeks.org/how-to-convert-categorical-variable-to-numeric-in-pandas/
"""

def dummies(x):  # x is a feature
  dummy = pd.get_dummies(df[x])
  df.drop(columns=x, inplace=True)
  return pd.concat([df, dummy], axis = 1)

df =  dummies('COUNTRY')

df =  dummies('DEALSIZE')

df =  dummies('PRODUCTLINE')

df.head(5)

df.dtypes

"""PRODUCTCODE datatype :

Using the standard pandas Categorical constructor, we can create a category object.
"""

cat = pd.Categorical(df['PRODUCTCODE'])
cat

"""Codes are an array of integers which are the positions of the actual values in the categories array."""

df['PRODUCTCODE'] = pd.Categorical(df['PRODUCTCODE']).codes

df

df.shape

"""drop 'ORDERDATE', 'QTR_ID' because we have 'MONTH' etc."""

df.drop('QTR_ID', axis=1, inplace=True)

df.shape

"""Use K-MEANS algorithm"""

from sklearn.preprocessing import StandardScaler
scaler =  StandardScaler()
df_scaled = scaler.fit_transform(df)

from sklearn.cluster import KMeans
scores = []
range_values = range(1, 15)
for i in range_values:
  kmeans = KMeans(n_clusters = i)
  kmeans.fit(df_scaled)
  scores.append(kmeans.inertia_)

  # Inertia measures how well a dataset was clustered by K-Means. 
  # It is calculated by 
  # measuring the distance between each data point and its centroid, squaring this distance,
  #  and summing these squares across one cluster.

plt.plot(scores, 'bx-') # bx is blue line and x on it and - is solid line
plt.title('Finding right number of clusters')
plt.xlabel('Clusters')
plt.ylabel('scores') 
plt.show();

#The elbow curve
plt.figure(figsize=(12,6))
plt.plot(range(1,15),scores)
plt.plot(range(1,15),scores, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
# plt.xticks(np.arange(1,15,1))
plt.ylabel("scores")

#Taking 3 clusters
km1=KMeans(n_clusters=3)
#Fitting the input data
km1.fit(df_scaled)
#predicting the labels of the input data
y=km1.predict(df_scaled)
#adding the labels to a column named label
df["cluster"] = y
#The new dataframe with the clustering done
df.head()

df.YEAR_ID.unique()

#Scatterplot of the clusters
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'YEAR_ID',y = 'SALES',hue="cluster",data = df )
plt.xlabel('YEAR_ID')
plt.ylabel('SALES') 
plt.title('SALES vs YEAR_ID')
plt.show()
# ,  palette=['green','dodgerblue','red'], legend='full',

df.MONTH_ID.unique()

#Taking 12 clusters
km1=KMeans(n_clusters=12)
#Fitting the input data
km1.fit(df_scaled)
#predicting the labels of the input data
y=km1.predict(df_scaled)
#adding the labels to a column named label
df["cluster"] = y
#The new dataframe with the clustering done
df.head()


#Scatterplot of the clusters
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'MONTH_ID',y = 'SALES',hue="cluster",data = df  )
plt.xlabel('MONTH_ID')
plt.ylabel('SALES') 
plt.title('SALES vs MONTH_ID')
plt.show()

from sklearn.cluster import KMeans
scores=[]
for i in range(1,15):
  kmeans=KMeans(n_clusters=i)
  kmeans.fit(df_scaled)
  scores.append(kmeans.inertia_)