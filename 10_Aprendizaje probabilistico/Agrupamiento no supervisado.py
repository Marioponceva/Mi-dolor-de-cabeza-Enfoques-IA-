#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: Agrupamiento no supervisado

from sklearn.cluster import KMeans
import numpy as np

# Generamos datos aleatorios para clusterizar
X = np.random.rand(100, 2)

# Instanciamos el modelo de K-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

# Entrenamos el modelo con los datos
kmeans.fit(X)

# Obtenemos las etiquetas de los clusters para cada dato
labels = kmeans.labels_

# Imprimimos los centroides de cada cluster
print(kmeans.cluster_centers_)

# Imprimimos las etiquetas de los clusters para cada dato
print(labels)