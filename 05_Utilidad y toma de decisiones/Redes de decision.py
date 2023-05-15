#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Utilidad y toma de decisiones
#Tema: Redes de decision

import matplotlib.pyplot as plt

class NodoDecision:
    def __init__(self, pregunta, respuesta_si=None, respuesta_no=None):
        self.pregunta = pregunta
        self.respuesta_si = respuesta_si
        self.respuesta_no = respuesta_no

def dibujar_arbol(nodo, ax=None, x=0, y=0, nivel=1):
    if ax is None:
        fig, ax = plt.subplots()
        ax.set_axis_off()

    ax.text(x, y, nodo.pregunta, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    if nodo.respuesta_si is not None:
        ax.plot([x, x - 0.5 ** nivel], [y, y - 1], '-k')
        dibujar_arbol(nodo.respuesta_si, ax, x - 0.5 ** nivel, y - 1, nivel + 1)

    if nodo.respuesta_no is not None:
        ax.plot([x, x + 0.5 ** nivel], [y, y - 1], '-k')
        dibujar_arbol(nodo.respuesta_no, ax, x + 0.5 ** nivel, y - 1, nivel + 1)

# Crear la red de decisiones
nodo_1 = NodoDecision("¿Tiene hambre?")
nodo_2 = NodoDecision("¿Desea una pizza?")
nodo_3 = NodoDecision("¿Desea una hamburguesa?")
nodo_4 = NodoDecision("¿Prefiere jamón y piña?")
nodo_5 = NodoDecision("¡Pida una pizza de jamón y piña!")
nodo_6 = NodoDecision("¡Pida una pizza de pepperoni!")
nodo_7 = NodoDecision("¡Pida una hamburguesa con queso!")

nodo_1.respuesta_si = nodo_2
nodo_1.respuesta_no = nodo_3
nodo_2.respuesta_si = nodo_4
nodo_2.respuesta_no = nodo_6
nodo_3.respuesta_si = nodo_7
nodo_3.respuesta_no = nodo_6
nodo_4.respuesta_si = nodo_5
nodo_4.respuesta_no = nodo_5

# Dibujar el árbol
dibujar_arbol(nodo_1)
plt.show()