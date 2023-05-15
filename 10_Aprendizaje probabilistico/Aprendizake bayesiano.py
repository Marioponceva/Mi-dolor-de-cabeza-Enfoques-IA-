#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: Aprendizake bayesiano

from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos Iris
data = load_iris()

# Dividimos el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Creamos el clasificador de Naive Bayes
clf = GaussianNB()

# Entrenamos el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Realizamos la predicción con los datos de prueba
y_pred = clf.predict(X_test)

# Medimos la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Imprimimos la precisión obtenida
print("Precisión:", accuracy)