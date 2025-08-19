# Sistema de Encuestas Dinámico Mejorado - Varias encuestas y preguntas
from collections import Counter

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

# Función para seleccionar encuesta
def seleccionar_encuesta():
    if not listar_encuestas():
        return None
    try:
        seleccion = int(input("Seleccione la encuesta (número): ")) - 1
        if 0 <= seleccion < len(encuestas):
            return encuestas[seleccion]
        else:
            print("Número de encuesta inválido.")
            return None
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return None

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

#Función buscar encuesta
def buscar_encuesta():
    if len(encuestas) == 0:
        print("No hay encuestas disponibles.")
    else:
        nombre_buscar = input("Ingrese el nombre de la encuesta a buscar: \n").strip().lower()
        encontrada = False

        for i, encuesta in enumerate(encuestas, start=1):
            if encuesta["nombre"].lower() == nombre_buscar:
                print(f"\nEncuesta encontrada: {encuesta['nombre']}")
                print("Preguntas:")
                for j, pregunta in enumerate(encuesta["preguntas"], start=1):
                    print(f"{i}. {pregunta[f'pregunta{j}']}")
                encontrada = True
                break

        if not encontrada:
            print("No se encontró ninguna encuesta con ese nombre.")

#funcion la cual borrar las respuestas de las preguntas
def borrar_respuestas():
    encuesta = seleccionar_encuesta()
    if not encuesta:
        return
    
    print("\n1. Borrar todas las respuestas de la encuesta\n2. Borrar respuestas de una pregunta específica")
    opcion = input("Seleccione una opción: \n").strip()
    
    if opcion == "1":
        for pregunta in encuesta["preguntas"]:
            pregunta["respuestas"] = []
        print("Todas las respuestas de la encuesta han sido eliminadas\n")
    
    elif opcion == "2":
        for idx, pregunta in enumerate(encuesta["preguntas"], start=1):
            print(f"{idx}. {pregunta[f'pregunta{idx}']}")
        try:
            n = int(input("Seleccione el número de pregunta: ")) - 1
            if 0 <= n < len(encuesta["preguntas"]):
                encuesta["preguntas"][n]["respuestas"] = []
                print("Respuestas de la pregunta eliminadas\n")
            else:
                print("Número de pregunta inválido.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
    else:
        print("Opción no válida.")



# funcion que muestra  estadisticas
def mostrar_resultados():
    if len(encuestas) == 0:
        print("No existen encuestas registradas")
    else:
        print("Encuestas: \n")
        for i, encuesta in enumerate(encuestas, start=1):
            print(f"{i}. {encuesta['nombre']}\n")

            if len(encuesta["preguntas"])>0:
                print("Preguntas: \n")

                for j, pregunta in enumerate(encuesta["preguntas"], start=1):
                    texto_pregunta = pregunta[f"pregunta{j}"]
                    print(f"   {j}. {texto_pregunta}\n   Respuestas:")

                    if len(pregunta["respuestas"]) > 0:
                        todas_respuestas = []
                        for k, r in enumerate(pregunta["respuestas"], start=1):
                            for usuario, respuesta in r.items():
                                print(f"      {k}. Usuario: {usuario} - Respuesta: {respuesta}")
                                todas_respuestas.append(respuesta.lower().strip())

                        # Estadísticas automáticas
                        print("Estadísticas:")
                        conteo = Counter(todas_respuestas)
                        total = sum(conteo.values())
                        for resp, cantidad in conteo.items():
                            porcentaje = (cantidad / total) * 100
                            print(f"      - {resp}: {cantidad} respuestas ({porcentaje:.1f}%)")
                    else:
                        print(f"No existen respuestas registradas para esta pregunta")
            else:
                print("No existen preguntas registradas en esta encuesta")
                print("-"*30)