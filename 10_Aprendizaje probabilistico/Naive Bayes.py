#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: Naive Bayes

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Creamos el vectorizador y transformamos los textos de entrenamiento
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(["Este es un texto de ejemplo", "Otro texto de ejemplo", "Y otro más"])

# Definimos las etiquetas de cada texto de entrenamiento
y_train = ["categoria 1", "categoria 2", "categoria 2"]

# Creamos el clasificador Naive Bayes y lo entrenamos
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Clasificamos nuevos textos
X_new = vectorizer.transform(["Texto a clasificar"])
predicted = clf.predict(X_new)

# Imprimimos la categoría predicha
print(predicted)