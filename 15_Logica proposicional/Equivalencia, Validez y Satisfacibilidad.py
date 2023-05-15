#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Logica
#Logica Proposicional
#Tema: Equivalencia, ,validez y satisfacibilidad

"""Teoria:
  En lógica proposicional, la equivalencia, validez y satisfacibilidad son conceptos 
  fundamentales para evaluar la calidad de las afirmaciones lógicas y las bases de 
  conocimiento.

Equivalencia: Dos expresiones lógicas son equivalentes si tienen el mismo valor 
de verdad para todas las combinaciones posibles de valores de verdad de sus variables 
proposicionales. En otras palabras, dos expresiones son equivalentes si siempre son 
verdaderas o siempre son falsas en las mismas circunstancias. Por ejemplo, 
las expresiones "p ∧ q" y "q ∧ p" son equivalentes porque tienen el mismo valor de 
verdad para todas las combinaciones de valores de verdad de "p" y "q".

Validez: Una expresión lógica es válida si es verdadera para todas las combinaciones 
posibles de valores de verdad de sus variables proposicionales. Es decir, si su valor 
de verdad es siempre verdadero, independientemente de los valores de verdad de las variables. 
Por ejemplo, la expresión "p ∨ ¬p" es válida porque es verdadera para cualquier valor de verdad de "p".

Satisfacibilidad: Una expresión lógica es satisfacible si existe al menos una combinación 
de valores de verdad de sus variables proposicionales que hace que la expresión sea verdadera. 
En otras palabras, una expresión es satisfacible si existe al menos una forma de asignar 
valores de verdad a sus variables para que la expresión sea verdadera. Por ejemplo, la expresión 
"p ∧ q" es satisfacible porque es verdadera cuando tanto "p" como "q" son verdaderos.
  """
import sympy

# Ejemplo de equivalencia
expresion1 = (3 + 2) == (2 + 3)
expresion2 = 5 == 5
equivalencia = expresion1 == expresion2
print("Equivalencia:", equivalencia)

# Ejemplo de validez
expresion3 = (4 < 5) or (5 < 4)
validez = expresion3
print("Validez:", validez)

# Ejemplo de satisfacibilidad
expresion4 = (1 > 0) and (9 < 10)
satisfacibilidad = sympy.satisfiable(expresion4)
print("Satisfacibilidad:", satisfacibilidad)