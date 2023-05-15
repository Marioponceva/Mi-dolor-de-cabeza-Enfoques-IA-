#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Razonamiento probabilistico en el tiempo
#Tema: Red Bayes Dinamica Filtrado de Particulas

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy.random import randn

# Definir el modelo
def transition_model(x, u):
    # Modelo de transición: random walk con una leve desviación
    return x + (randn() * 0.1) + u

def observation_model(x):
    # Modelo de observación: Gaussiana con media x y desviación estándar 0.1
    return norm(x, 0.1).rvs()

# Definir el número de partículas
N = 1000

# Inicializar las partículas
particles = np.zeros((N, 2))
particles[:, 0] = np.random.normal(0, 1, N)
weights = np.ones(N) / N

# Inicializar la estimación
x_est = np.zeros(2)

# Definir la trayectoria de entrada
U = np.zeros((100, 2))
U[:, 0] = 0.2 * np.sin(np.linspace(0, 6 * np.pi, 100))
U[:, 1] = 0.2 * np.cos(np.linspace(0, 6 * np.pi, 100))

# Simulación
for t in range(len(U)):
    # Predecir la posición de las partículas
    for i in range(N):
        particles[i, 1] = transition_model(particles[i, 0], U[t, 0])
        particles[i, 0] = transition_model(particles[i, 1], U[t, 1])
    
    # Calcular las observaciones
    observations = np.array([observation_model(particles[i, 0]) for i in range(N)])
    
    # Calcular los pesos
    weights *= norm.pdf(observations, loc=particles[:, 0], scale=0.1)
    weights /= np.sum(weights)
    
    # Estimar la posición del robot
    x_est = np.average(particles, weights=weights, axis=0)
    
    # Mostrar los resultados
    print("Tiempo:", t)
    print("Posición del robot estimada:", x_est)
    print("Posición del robot real:", U[t])
    print()
    
    # Re-muestrear las partículas
    indices = np.random.choice(N, size=N, p=weights)
    particles = particles[indices]
    weights = np.ones(N) / N