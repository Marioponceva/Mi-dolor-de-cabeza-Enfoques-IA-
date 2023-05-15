#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Percepcion
#Tema: Etiquetado de lineas

"""Teoria:
    El etiquetado de líneas de texto, también conocido como etiquetado de secuencias, es una técnica utilizada 
    en el procesamiento de lenguaje natural (NLP) que consiste en asignar una etiqueta a cada elemento en una 
    secuencia de texto. Esta técnica es ampliamente utilizada para tareas de NLP como el reconocimiento de entidades 
    nombradas, el etiquetado de partes del discurso y la segmentación de oraciones.

En el enfoque de probabilidad en IA, el etiquetado de líneas de texto se puede lograr mediante el uso de modelos 
de aprendizaje automático, como los modelos de Markov ocultos (HMM) o las redes neuronales recurrentes (RNN). 
Estos modelos se entrenan en conjuntos de datos etiquetados previamente para aprender patrones y relaciones 
entre las palabras y las etiquetas. Luego, se pueden utilizar para predecir las etiquetas de nuevas secuencias 
de texto no etiquetadas en función de la probabilidad de que una etiqueta dada aparezca en una determinada posición 
en la secuencia.
    """

import nltk  # Importamos la biblioteca NLTK

#Guardamos la oracion en una variable string
oracion = "The cat is always sleeping"
#Tokenizamos la oracion (la dividimos en palabras para despues etiquetarla)
tokens = nltk.word_tokenize(oracion)

# Etiquetamos las partes de la oracion
etiquetado = nltk.pos_tag(tokens)

# Imprimimos los resultados
print(etiquetado)
