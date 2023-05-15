#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Enfoque: Probabilidad
#Razonamiento probabilistico en el tiempo
#Tema: Reconocimiento del habla

import speech_recognition as sr

# Creamos un objeto recognizer
r = sr.Recognizer()

# Definimos la fuente de audio, en este caso utilizamos el micrófono
with sr.Microphone() as source:
    print("Habla ahora...")
    # Escuchamos el audio del micrófono
    audio = r.listen(source)

try:
    # Utilizamos la función recognize_google para convertir el audio a texto utilizando el servicio de Google
    text = r.recognize_google(audio, language="es-ES")
    print("Google Speech Recognition ha interpretado: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition no ha podido entender el audio")
except sr.RequestError as e:
    print("No se puede conectar con el servicio de Google Speech Recognition; {0}".format(e))