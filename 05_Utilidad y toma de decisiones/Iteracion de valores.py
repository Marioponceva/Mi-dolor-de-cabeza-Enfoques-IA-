#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: Iteracion de valores

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random


def bfs(graph, start_node, target):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == target:
            return True

        visited.add(node)
        neighbors = graph[node]

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    return False


# Generar un grafo aleatorio utilizando NetworkX
num_nodes = 10  # Número de nodos
prob = 0.3  # Probabilidad de crear un borde entre dos nodos
random_graph = nx.fast_gnp_random_graph(num_nodes, prob, directed=True)

# Convertir el grafo aleatorio en un diccionario de listas de adyacencia
graph = {str(node): [str(neighbor) for neighbor in neighbors] for node, neighbors in random_graph.adj.items()}

start_node = random.choice(list(graph.keys()))
target_node = random.choice(list(graph.keys()))

# Crear el grafo dirigido utilizando NetworkX
G = nx.DiGraph(graph)

# Obtener el trazado del grafo
pos = nx.spring_layout(G)

# Etiquetas de nodos
labels = {node: node for node in G.nodes}

# Colores de nodos
node_colors = ['lightblue' if node == start_node else 'lightgreen' if node == target_node else 'lightgray' for node in G.nodes]

# Colores de bordes
edge_colors = ['black' if bfs(graph, start_node, target_node) else 'lightgray' for _, _ in G.edges]

# Dibujar el grafo
nx.draw_networkx(G, pos, labels=labels, node_color=node_colors, edge_color=edge_colors, arrows=True)
plt.axis('off')
plt.show()
