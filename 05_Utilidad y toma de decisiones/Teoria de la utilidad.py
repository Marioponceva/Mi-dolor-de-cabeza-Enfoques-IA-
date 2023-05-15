#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: Teoria de la utilidad

import heapq


def dijkstra(graph, start):
    # Inicializar las estructuras de datos
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # Si ya hemos encontrado un camino más corto a este nodo, ignorarlo
        if current_dist > distances[current_node]:
            continue

        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            utility = calculate_utility(weight)  # Calcular la utilidad para la arista

            # Calcular la utilidad acumulada para el vecino
            neighbor_utility = distances[current_node] + utility

            # Si encontramos un camino más útil hacia el vecino, actualizar la distancia y agregarlo a la cola
            if neighbor_utility < distances[neighbor]:
                distances[neighbor] = neighbor_utility
                heapq.heappush(queue, (neighbor_utility, neighbor))

    return distances


# Función de ejemplo para calcular la utilidad de una arista
def calculate_utility(weight):
    # Aquí puedes implementar tu propia función de cálculo de utilidad según tus necesidades
    return 1 / weight


# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'D': 1},
    'D': {'E': 1},
    'E': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Distancias más útiles desde el nodo inicial:")
for node, distance in distances.items():
    print(f"Nodo: {node}, Distancia: {distance}")