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






# Función para registrar respuestas
def registrar_respuesta():
    encuesta = seleccionar_encuesta()
    if not encuesta:
        return

    usuario = input("Ingrese su nombre: \n")

    if len(encuesta["preguntas"]) == 0:
        print("No hay preguntas en esta encuesta")
        return

    for idx, pregunta in enumerate(encuesta["preguntas"], start=1):
        texto_pregunta = pregunta[f"pregunta{idx}"]
        print(f"{idx}. {texto_pregunta}")
        respuesta = input("Ingrese su respuesta: \n")
        pregunta["respuestas"].append({usuario: respuesta})

    print("Respuestas registradas correctamente\n")
    
# Función para mostrar resultados
def mostrar_resultados():
    encuesta = seleccionar_encuesta()
    if not encuesta:
        return

    if len(encuesta["preguntas"]) == 0:
        print("No hay preguntas en esta encuesta")
        return

    print(f"\nResultados de la encuesta '{encuesta['nombre']}':\n")
    for numero_encuesta, pregunta in enumerate(encuesta["preguntas"], start=1):
        texto_pregunta = pregunta[f"pregunta{numero_encuesta}"]
        print(f"{numero_encuesta}. {texto_pregunta}")
        if len(pregunta["respuestas"]) > 0:
            for k, r in enumerate(pregunta["respuestas"], start=1):
                for usuario, respuesta in r.items():
                    print(f"   {k}. Usuario: {usuario} - Respuesta: {respuesta}")
        else:
            print("   No existen respuestas registradas para esta pregunta")
        print("-" * 30) # separador para dividir bien las encuestas
