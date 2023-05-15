#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: MDP Parcialmente Observable (POMDP)

import random
import networkx as nx
from time import sleep

# Generar grafo aleatorio con al menos un nodo sin vecinos
num_nodes = 10
graph = None
while True:
    graph = nx.fast_gnp_random_graph(num_nodes, 0.25)  # Ajusta el valor de p según sea necesario
    isolated_nodes = [node for node in graph.nodes if len(list(graph.neighbors(node))) == 0]
    if len(isolated_nodes) > 0:
        break

# Definir estado inicial y creencia inicial
current_state = random.choice(list(graph.nodes))
belief = {node: 1 / num_nodes for node in graph.nodes}

# Definir funciones de transición y observación aleatorias
def transition_model(current_state, action):
    neighbors = list(graph.neighbors(current_state))
    return random.choice(neighbors)

def observation_model(current_state):
    return current_state

# Iterar en el proceso de decisión parcialmente observable
while True:
    sleep(0.5)
    print("Current state:", current_state)
    print("Belief:", belief)

    # Tomar acción basada en la creencia actual
    action = random.choice(list(graph.neighbors(current_state)))

    # Observar el estado parcialmente
    observation = observation_model(current_state)

    # Actualizar la creencia utilizando el modelo de transición y observación
    new_belief = {}
    for node in graph.nodes:
        prior = belief[node]
        likelihood = 1 if node == observation else 0.1  # Simplified observation model
        transition_prob = 1 if node == transition_model(current_state, action) else 0.1  # Simplified transition model
        new_belief[node] = prior * likelihood * transition_prob
    total_belief = sum(new_belief.values())
    belief = {node: new_belief[node] / total_belief for node in graph.nodes}

    # Actualizar el estado actual en función de la acción tomada
    current_state = transition_model(current_state, action)

    # Condición de terminación (llegar a un nodo sin vecinos)
    if len(list(graph.neighbors(current_state))) == 1:
        break
