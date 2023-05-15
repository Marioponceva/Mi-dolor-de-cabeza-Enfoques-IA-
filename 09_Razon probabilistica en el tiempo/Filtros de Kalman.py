#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Razonamiento probabilistico en el tiempo
#Tema: Filtros-de-Kalman

import numpy as np
import matplotlib.pyplot as plt

# Definimos las matrices de estado y medición
A = np.array([[1, 1], [0, 1]])  # Matriz de estado
C = np.array([[1, 0]])  # Matriz de medición

# Definimos las matrices de ruido del proceso y de la medición
Q = np.array([[0.1, 0.1], [0.1, 0.1]])
R = np.array([[1]])

# Generamos una trayectoria aleatoria de posición y velocidad
np.random.seed(0)
n_steps = 50
dt = 0.1
pos_true = np.zeros(n_steps)
vel_true = np.zeros(n_steps)
pos_meas = np.zeros(n_steps)
for i in range(1, n_steps):
    vel_true[i] = 0.5 * vel_true[i-1] + 0.1 * np.random.randn()
    pos_true[i] = pos_true[i-1] + vel_true[i-1]*dt
    pos_meas[i] = pos_true[i] + np.sqrt(R[0,0]) * np.random.randn()

# Definimos el vector de estado inicial y la matriz de covarianza inicial
x0 = np.array([pos_meas[0], 0])
P0 = np.array([[10, 0], [0, 1]])

# Ejecutamos el filtro de Kalman para estimar la posición y velocidad
x_est = np.zeros((n_steps, 2))
P_est = np.zeros((n_steps, 2, 2))
x_est[0] = x0
P_est[0] = P0
for i in range(1, n_steps):
    # Predicción del estado y de la covarianza
    x_pred = A @ x_est[i-1]
    P_pred = A @ P_est[i-1] @ A.T + Q

    # Actualización del estado y de la covarianza
    y = pos_meas[i] - C @ x_pred
    S = C @ P_pred @ C.T + R
    K = P_pred @ C.T @ np.linalg.inv(S)
    x_est[i] = x_pred + K @ y
    P_est[i] = (np.eye(2) - K @ C) @ P_pred

# Graficamos la trayectoria estimada junto con la trayectoria real
plt.figure(figsize=(8, 6))
plt.plot(np.arange(n_steps)*dt, pos_true, label='Posición real')
plt.plot(np.arange(n_steps)*dt, x_est[:, 0], label='Posición estimada')
plt.legend()
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.show()