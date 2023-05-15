#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: k-NN, k-Medias y Clustering

import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generar datos de prueba
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=0)

# Algoritmo k-NN
nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)

print('Distancias:', distances)
print('Indices vecinos:', indices)

# Algoritmo k-Medias
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print('Labels:', labels)
print('Centroides:', centroids)

# Algoritmo de Clustering
from sklearn.cluster import AgglomerativeClustering
agg_clustering = AgglomerativeClustering(n_clusters=4).fit(X)
print('Etiquetas Clustering Aglomerativo:', agg_clustering.labels_)
