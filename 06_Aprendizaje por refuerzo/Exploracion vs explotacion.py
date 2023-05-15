#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Aprendizaje por refuerzo
#Tema: Exploracion vs explotacion

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

    def explore(self, node):
        print("Exploring node:", node)

        if node in self.graph:
            neighbors = self.graph[node]
            for neighbor in neighbors:
                self.explore(neighbor)

    def exploit(self, node):
        print("Exploiting node:", node)

        if node in self.graph:
            neighbors = self.graph[node]
            best_neighbor = max(neighbors)  # Ejemplo de explotación: selecciona el vecino con el valor máximo
            self.exploit(best_neighbor)

# Crear un grafo de ejemplo
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

# Ejemplo de exploración
print("=== Exploración ===")
graph.explore(1)

# Ejemplo de explotación
print("=== Explotación ===")
graph.exploit(1)