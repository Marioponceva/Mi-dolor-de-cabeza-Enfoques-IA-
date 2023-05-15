#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Aprendizaje por refuerzo
#Tema: Busqueda de la politica

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random

def buscar_politica(grafo, inicio, objetivo):
    camino = {}
    cola = deque()
    cola.append(inicio)
    while cola:
        nodo_actual = cola.popleft()
        if nodo_actual == objetivo:
            break
        for vecino in grafo[nodo_actual]:
            if vecino not in camino:
                camino[vecino] = nodo_actual
                cola.append(vecino)
    ruta = []
    nodo = objetivo
    while nodo != inicio:
        ruta.append(nodo)
        nodo = camino[nodo]
    ruta.append(inicio)
    ruta.reverse()
    return ruta

# Crear un grafo aleatorio
grafo = nx.gnp_random_graph(10, 0.3, directed=False)
inicio = random.choice(list(grafo.nodes))
objetivo = random.choice(list(grafo.nodes))
while inicio == objetivo:
    objetivo = random.choice(list(grafo.nodes))

# Encontrar el camino utilizando la búsqueda de política
politica = buscar_politica(grafo, inicio, objetivo)
print("Camino:", politica)

# Visualizar el grafo y el camino resultante
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_nodes(grafo, pos, nodelist=politica, node_color='red')
nx.draw_networkx_edges(grafo, pos, edgelist=[(politica[i], politica[i+1]) for i in range(len(politica)-1)], edge_color='red', width=2)
plt.title("Grafo y camino resultante")
plt.show()