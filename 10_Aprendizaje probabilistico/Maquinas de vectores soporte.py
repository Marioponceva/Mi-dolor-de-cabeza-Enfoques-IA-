#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Aprendizaje probabilistico
#Tema: Maquinas de vectores soporte

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargar conjunto de datos
iris = datasets.load_iris()

# Separar en características y etiquetas
X = iris.data
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador SVM
svm_clf = SVC(kernel='linear')

# Entrenar el clasificador con los datos de entrenamiento
svm_clf.fit(X_train, y_train)

# Hacer predicciones con los datos de prueba
y_pred = svm_clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
print("Precisión del modelo SVM:", accuracy)