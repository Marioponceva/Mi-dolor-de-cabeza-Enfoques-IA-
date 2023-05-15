#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: Red bayesiada dinamica

import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.DiGraph()

# Definir los estados del clima
clima = ['soleado', 'nublado', 'lluvioso']

# Añadir los nodos al grafo
for i in range(len(clima)):
    G.add_node(i, label=clima[i])

# Añadir los arcos al grafo
for i in range(1, len(clima)):
    G.add_edge(i-1, i)

# Dibujar el grafo
labels = nx.get_node_attributes(G, 'label')
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
nx.draw_networkx_labels(G, pos, labels)
plt.show()