# Sistema de Encuestas Dinámico Mejorado - Varias encuestas y preguntas

print("Bienvenido al Sistema de Encuestas Dinámico\n")

# Lista para almacenar encuestas
encuestas = []

# Función para crear una encuesta
def crear_encuesta():
    nombre = input("Ingrese el nombre de la encuesta: \n")
    encuesta = {
        "nombre": nombre,
        "preguntas": []
    }

    i = 1
    while True:
        pregunta = input(f"Ingrese la pregunta {i} (o escriba 'fin' para terminar): \n")
        if pregunta.lower().strip() == "fin":
            if len(encuesta["preguntas"]) == 0:
                print("Debe ingresar al menos una pregunta.")
                continue
            break

        pregunta_dic = {
            f"pregunta{i}": pregunta,
            "respuestas": []  # Guardar respuestas de los usuarios
        }

        encuesta["preguntas"].append(pregunta_dic)
        i += 1

    encuestas.append(encuesta)
    print(f"Encuesta '{nombre}' creada con éxito\n")

# Función para listar encuestas
def listar_encuestas():
    if len(encuestas) == 0:
        print("No hay encuestas disponibles.")
        return False

    print("\nEncuestas disponibles:")
    for i, encuesta in enumerate(encuestas, start=1):
        print(f"{i}. {encuesta['nombre']}")
    return True
