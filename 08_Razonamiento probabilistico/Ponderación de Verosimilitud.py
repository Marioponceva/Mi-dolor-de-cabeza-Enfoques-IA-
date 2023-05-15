#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Razonamiento probabilistico
#Tema: Ponderación de Verosimilitud

import numpy as np

# Definir el conjunto de observaciones
observaciones = ['Cara', 'Cara', 'Cruz', 'Cara']

# Definir el conjunto de pesos para cada observación
pesos = [0.2, 0.3, 0.5, 0.4]

# Calcular la probabilidad ponderada de obtener una cara
probabilidad = np.sum(np.array(observaciones) == 'Cara' * np.array(pesos)) / np.sum(pesos)

print("La probabilidad ponderada de obtener una cara es:", probabilidad)