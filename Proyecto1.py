#Sistema de Encuestas Dinámico
print("Bienvenido al Sistema de Encuestas Dinámico\n")

# Creamos una lista en donde se van a almacenar las encuestas
encuestas = []

# Función para crear una encuesta
def crear_encuesta():
    nombre = input("Ingrese el nombre de la encuesta: \n")
    encuesta = {
        "nombre": nombre,
        "preguntas": []
    }

    i = 1
    #Creamos un bucle para ir agregando las preguntas
    while True:
        pregunta = input("Ingrese la pregunta (o escriba 'fin' para terminar): \n")
        if pregunta.lower().strip() == "fin":
            break

        preguntas = {
            f"pregunta{i}": pregunta,
            "respuestas": []  # Aquí se van a guardar las respuestas de los usuarios
        }

        encuesta["preguntas"].append(preguntas)
        i += 1

    encuestas.append(encuesta)
    print("Encuesta creada con éxito")

print("Prueba 3")