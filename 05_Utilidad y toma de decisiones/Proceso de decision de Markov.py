#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: Proceso de decision de Markov

import random
import networkx as nx
from time import sleep

# Generar grafo aleatorio
num_nodes = 10
graph = nx.fast_gnp_random_graph(num_nodes, 0.25)

# Asignar probabilidades de transición aleatorias
transition_matrix = {}
for node in graph.nodes:
    neighbors = list(graph.neighbors(node))
    probabilities = [random.random() for _ in range(len(neighbors))]
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]
    transition_matrix[node] = dict(zip(neighbors, probabilities))

# Definir estado inicial
current_node = random.choice(list(graph.nodes))

# Iterar en el proceso de decisión
while True:
    sleep(0.5)
    print("Current node:", current_node)

    # Obtener probabilidades de transición del nodo actual
    probabilities = transition_matrix[current_node]
    next_node = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]

    # Actualizar nodo actual
    current_node = next_node

    # Condición de terminación (puede personalizarse según tus necesidades)
    if len(list(graph.neighbors(current_node))) == 1:
        break