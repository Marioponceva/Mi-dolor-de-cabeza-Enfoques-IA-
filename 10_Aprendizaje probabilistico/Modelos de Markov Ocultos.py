#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: Modelos de Markov Ocultos

from hmmlearn import hmm
import numpy as np

# Datos de entrenamiento
obs = np.array([[0.5], [1.0], [-0.3], [-1.5], [0.0]])

# Definir el modelo
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Entrenar el modelo
model.fit(obs)

# Predecir la secuencia de estados ocultos más probable para una nueva secuencia de observaciones
obs_new = np.array([[0.8], [-0.7], [0.2]])
logprob, state_sequence = model.decode(obs_new)

print("Log-probabilidad de la secuencia:", logprob)
print("Secuencia de estados ocultos más probable:", state_sequence)