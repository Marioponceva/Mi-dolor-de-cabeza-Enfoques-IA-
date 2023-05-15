#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Logica
#Logica Proposicional
#Tema: Base de conocimiento

"""Teoria:
  La base de conocimiento en lógica proposicional se utiliza 
  en sistemas de inteligencia artificial para razonar sobre el 
  conocimiento y tomar decisiones. Al combinar las declaraciones 
  en la base de conocimiento con hechos y reglas adicionales, se
  pueden generar conclusiones y recomendaciones útiles.
    """
# Definición de la base de conocimiento
base_conocimiento = {
    "p": True,       # "p" es verdadero
    "q": False       # "q" es falso
}

# Ejemplo de uso de la base de conocimiento
if base_conocimiento["p"] and not base_conocimiento["q"]:
    print("p es verdadero y q es falso")
else:
    print("No se cumple la condición")
