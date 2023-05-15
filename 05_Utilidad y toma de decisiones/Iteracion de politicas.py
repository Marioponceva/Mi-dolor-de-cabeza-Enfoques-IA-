#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: Iteracion de politicas

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, probability):
    G = nx.erdos_renyi_graph(num_nodes, probability)
    return G

def initialize_policy(graph):
    policy = {}
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        num_neighbors = len(neighbors)
        if num_neighbors > 0:
            random_action = np.random.choice(neighbors)
            policy[node] = random_action
    return policy

def value_iteration(graph, policy, gamma, max_iterations):
    V = {node: 0 for node in graph.nodes}

    for _ in range(max_iterations):
        new_V = V.copy()

        for node in graph.nodes:
            action = policy[node]
            neighbors = list(graph.neighbors(node))
            num_neighbors = len(neighbors)

            if num_neighbors > 0:
                next_node = action
                reward = graph[node][next_node]['weight']
                new_V[node] = reward + gamma * V[next_node]

        V = new_V

    return V

def find_best_path(graph, start_node, end_node, values):
    current_node = start_node
    path = [current_node]

    while current_node != end_node:
        neighbors = list(graph.neighbors(current_node))
        if len(neighbors) > 0:
            next_node = max(neighbors, key=lambda n: values[n])
            path.append(next_node)
            current_node = next_node
        else:
            break

    return path

# Generar un grafo aleatorio
num_nodes = 10
probability = 0.3
graph = generate_random_graph(num_nodes, probability)

# Asignar pesos aleatorios a las aristas
for edge in graph.edges:
    weight = np.random.randint(1, 10)
    graph[edge[0]][edge[1]]['weight'] = weight

# Inicializar la política
policy = initialize_policy(graph)

# Parámetros del algoritmo de iteración de políticas
gamma = 0.9
max_iterations = 10

# Aplicar la iteración de políticas
values = value_iteration(graph, policy, gamma, max_iterations)

# Encontrar el mejor camino entre dos nodos
start_node = 0
end_node = 9
best_path = find_best_path(graph, start_node, end_node, values)

# Graficar el grafo y el mejor camino
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos=pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))
nx.draw_networkx_nodes(graph, pos=pos, nodelist=best_path, node_color='red')
nx.draw_networkx_edges(graph, pos=pos, edgelist=list(zip(best_path, best_path[1:])), edge_color='red', width=2)
plt.title('Grafo aleatorio con mejor camino entre nodos {} y {}'.format(start_node, end_node))
plt.show()