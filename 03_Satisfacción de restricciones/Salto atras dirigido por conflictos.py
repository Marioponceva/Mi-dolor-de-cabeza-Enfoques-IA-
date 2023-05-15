#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Busqueda en grafos
#Satisfaccion de restricciones
#Tema: Salto atras dirigido por conflictos

from typing import Dict, List, Optional

# Ejemplo de restricciones
constraints = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
}

# Función para buscar soluciones utilizando backtracking con conflictos
def backtrack(assignment: Dict[str, int], unassigned: List[str], constraints: Dict[str, List[str]]) -> Optional[Dict[str, int]]:
    if not unassigned:
        # Se encontró una solución, retorna las asignaciones
        return assignment
    
    # Busca la variable no asignada con más restricciones
    var = max(unassigned, key=lambda v: len(constraints[v]))
    
    # Prueba con cada valor en el dominio de la variable
    for value in range(1, 6):
        if check_consistency(var, value, assignment, constraints):
            # La asignación es consistente, intenta con la siguiente variable
            assignment[var] = value
            unassigned.remove(var)
            result = backtrack(assignment, unassigned, constraints)
            if result is not None:
                # Se encontró una solución, retorna las asignaciones
                return result
            # Si la asignación no lleva a una solución, revierte los cambios
            assignment.pop(var)
            unassigned.append(var)
    
    # No se encontró ninguna solución
    return None

# Función auxiliar para verificar la consistencia de una asignación
def check_consistency(var: str, value: int, assignment: Dict[str, int], constraints: Dict[str, List[str]]) -> bool:
    for neighbor in constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            # La asignación no es consistente con una restricción
            return False
    # La asignación es consistente
    return True

# Ejemplo de uso
assignment = {}
unassigned = list(constraints.keys())
result = backtrack(assignment, unassigned, constraints)

if result is not None:
    # Se encontró una solución, imprime las asignaciones
    print("Solución encontrada:")
    for var, value in result.items():
        print(f"{var}: {value}")
else:
    # No se encontró ninguna solución
    print("No se encontró ninguna solución.")