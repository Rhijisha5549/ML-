# -*- coding: utf-8 -*-
"""Unsupervised ML

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eXj48XYQByS4rCGF0cunjuXj85XV_W7M

# **The Sparks Foundation - GRIP - Data Science and Business Analytics -July21**

**Task 2 : Prediction using unsupervised ML**

**Author : Rhijisha Dutta**

**Dataset used : iris dataset**

**Problem Statement :**


*   Predict the optimum number of clusters and represent it visualy.

**Import required libraries**
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import datasets

"""**Reading the data-set**"""

# Loading and Reading the iris dataset
data = pd.read_csv("iris.csv")
data

data.shape

data.head() # Loads the first five rows

data.tail() # Loads the last five rows

data.describe()

data.info()

# Check for nulls & duplicates
print(data.isnull().sum(), '\n\nNumber of duplicate rows:', data.duplicated().sum())

# drop duplicate rows
data.drop_duplicates(inplace=True)
data.shape[0]

"""**Now, let's check for uniquec classes in the dataset**"""

data.Species.unique()

# Distribution of features by Species

for i in data.columns[:-1]:
  sns.kdeplot(data = data.loc[data.Species=='Iris-setosa'][i], label = 'Iris-setosa', shade=True)
  sns.kdeplot(data = data.loc[data.Species=='Iris-versicolor'][i], label = 'Iris-versicolor', shade=True)
  sns.kdeplot(data = data.loc[data.Species=='Iris-virginica'][i], label = 'Iris-virginica', shade=True)
              
  plt.title(i);

  plt.show()

sns.set(style= 'whitegrid')
iris = sns.load_dataset('iris')
ax = sns.stripplot(x = 'species', y = 'sepal_length',data = iris);
plt.title('Iris Dataset')
plt.show()

sns.boxplot(x = 'species', y = 'sepal_width', data = iris)
plt.title("Iris Dataset")
plt.show()

sns.boxplot(x = 'species', y = 'petal_width', data = iris)
plt.title("Iris Dataset")
plt.show()

sns.boxplot(x = 'species', y = 'petal_length', data = iris)
plt.title("Iris Dataset")
plt.show()

sns.boxplot(x = 'species', y = 'sepal_length', data = iris)
plt.title("Iris Dataset")
plt.show()

# Count plot
sns.countplot(x = 'species', data=iris, palette='OrRd');
plt.title("Count of different species in Iris dataset")
plt.show()

# Correlation Matrix
data.corr()

# Heat Map
sns.heatmap(data.corr(), annot=True, cmap='RdYlGn')
plt.title("Heat-Map")
plt.show()

"""**Finding the optimum number of clusters using k-means clustering**"""

# Finding the optimum number of clusters for k-means classification

x = data.iloc[:, [0, 1, 2, 3]].values

from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', 
                    max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    # appending the WCSS to the list (kmeans.inertia_ returns the WCSS value for an initialized cluster)
    wcss.append(kmeans.inertia_)
    print('k:',i,"wcss:",kmeans.inertia_)

# Plotting the results onto a line graph, 
# `allowing us to observe 'The elbow'
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') # Within cluster sum of squares
plt.show()

"""We can see that after 3 the drop in WCSS is minimal So we choose 3 as the optimal number of clusters

**Initializing K-Means with Optimum Number Of Clusters**
"""

# Fitting K-Means to the Dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)

# Returns a label for each data point based on the number of clusters
y_kmeans = kmeans.fit_predict(x)

"""**Predicting Values**"""

y_kmeans

"""**Visualizing the Clusters**"""

# Visualising the clusters - On the first two columns
plt.figure(figsize=(10,10))
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1],  s = 100, c = 'blue', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1],s = 100, c = 'green', label = 'Iris-virginica')

# Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')
plt.title('Iris flower Clusters')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Petal Length in cm')
plt.legend()
plt.show()