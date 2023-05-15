#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: Algoritmo EM

from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generamos un conjunto de datos sintéticos con tres grupos distintos
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=0)

# Ajustamos un modelo de mezcla de Gaussianas utilizando el algoritmo EM
gmm = GaussianMixture(n_components=3, covariance_type='full', max_iter=100)
gmm.fit(X)

# Predecimos las etiquetas para los puntos de datos utilizando el modelo ajustado
y_pred = gmm.predict(X)

# Mostramos los resultados en la consola
print('Etiquetas verdaderas:')
print(y_true)
print('Etiquetas predichas:')
print(y_pred)