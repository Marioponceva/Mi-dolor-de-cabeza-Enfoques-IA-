#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Satisfaccion de restricciones
#Tema: Propagacion de restricciones

from constraint import *

# Creamos una instancia del solver de restricciones
problem = Problem()

# Definimos las variables del problema y sus posibles valores
problem.addVariable('x', [1, 2, 3])
problem.addVariable('y', [2, 3, 4])

# Definimos las restricciones del problema
def constraint_func(x, y):
    # La suma de x e y debe ser mayor o igual a 5
    return x + y >= 5

# Agregamos la restricción al problema
problem.addConstraint(constraint_func, ['x', 'y'])

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)


