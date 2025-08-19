# Sistema de Encuestas Dinámico

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de un sistema de encuestas dinámico en consola, nos va permitir crear encuestas personalizadas, registrar respuestas de los usuarios y mostrar resultados.
El sistema está diseñado para ser modular, fácil de usar y fuerte ante errores comunes y específicos, utilizando estructuras como funciones, ciclos, condicionales y manejo de excepciones.


## Objetivo
Desarrollar un sistema que permita:
- Crear encuestas de manera dinámica.
- Registrar respuestas de usuarios desde consola.
- Validar la entrada de datos y manejar errores.
- Mostrar los resultados de las encuestas de forma clara.
- Versátil con la finalidad de agregar nuevas funcionalidades.


## Integrantes del Equipo y Roles

1. Johann Herrera – Líder técnico
   - Organiza las tareas del equipo y asegura el uso correcto de
estructuras (ciclos, condicionales, manejo de errores).
   - Supervisa pull requests y aprueba cambios en GitHub. 

   Angel Rodas - Desarrollador principal  
   - Responsable del funcionamiento general del código.  
 

2. Juan Pablo Sánchez Santiagos – Responsable de pruebas y manejo de errores**  
   - Diseña pruebas para validar el sistema en distintos escenarios (entradas válidas, erróneas, vacías).  
   - Implementa y documenta excepciones en el código.  
   - Escribe un reporte de pruebas y resultados obtenidos.  

3. Alexis Lopez  – Encargado de interfaz de usuario y flujo
   - Diseña menús y navegación del programa.  
   - Garantiza una experiencia clara para el usuario en cada paso.  
   - Documenta el flujo del sistema (diagrama o pseudocódigo comentado).  

4. Johann Herrera – Gestor de documentación y repositorio**  
   - Mantiene actualizado el repositorio en GitHub.  
   - Redacta este archivo `README.md` e incluye instrucciones de uso, roles, problemas y soluciones.  
   - Se asegura de que los commits tengan mensajes claros.  
   - Sube documentación extra.  

5. Equipo completo – Apoyo en desarrollo y revisión cruzada
   - Colaboradores en la programación de funciones adicionales.  
   - Documentadores de sugerencias de mejora en la bitácora técnica.  

## Requisitos Técnicos
- Lenguaje: Python 3.13  
- Git y GitHub: control de versiones, al menos 5 commits por persona.  
- Uso de:
  - Funciones (modularidad del sistema).  
  - Ciclos y condicionales.  
  - Manejo de excepciones.  
  - Documentación técnica y de usuario.

# Sistema de Encuestas Dinámico

## Instrucciones de uso
1. Ejecutar el archivo `Proyecto1.py` en Python 3.x.
2. Al iniciar, se mostrará el menú principal con las siguientes opciones:
   - Crear encuesta
   - Registrar respuestas
   - Mostrar resultados
   - Buscar encuesta
   - Borrar respuestas
   - Mostrar estadísticas
   - Editar encuesta/pregunta
   - Eliminar encuesta
   - Salir
3. Seguir las indicaciones en pantalla para cada opción:
   - Ingresar nombres de encuestas y preguntas.
   - Registrar respuestas de usuarios.
   - Visualizar resultados y estadísticas.
   - Editar o borrar encuestas/preguntas según sea necesario.
4. Para salir del sistema, seleccionar la opción `0` en el menú principal.

## Vitacora de errores
| Problema | Solución |
|----------|----------|
| Uso de `try-except` para evitar errores al ingresar datos | Implementación de bloques `try-except` en entradas numéricas y de texto. |
| Conflictos al editar el código en GitHub sin ser el creador | Trabajar en ramas propias y solicitar merge de cambios. |
| Creación incorrecta de la carpeta `.git` fuera del proyecto | Inicializar Git dentro de la carpeta correcta del proyecto. |
| Divergencia de ramas y errores al hacer pull/push | Hacer pull o rebase antes de push, resolver conflictos y sincronizar ramas. |
| Errores de sintaxis olvidados (paréntesis, indentación, comillas, llaves) | Revisar cuidadosamente la sintaxis y corregir los errores antes de ejecutar el código. |
