class Trabajo:
    def __init__(self, nombre):
        self.nombre = nombre

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajo = None

class Trabajador:
    def __init__(self, persona, trabajo):
        self.persona = persona
        self.trabajo = trabajo

# Pregunta al usuario cuántas personas quiere crear
num_personas = int(input("¿Cuántas personas quieres crear? "))

personas = []
trabajos = []

# Crear personas
for i in range(num_personas):
    nombre_persona = input(f"Ingrese el nombre de la persona {i+1}: ")
    persona = Persona(nombre_persona)
    personas.append(persona)

# Pregunta al usuario cuántos trabajos quiere crear
num_trabajos = int(input("¿Cuántos trabajos quieres crear? "))

# Crear trabajos
for i in range(num_trabajos):
    nombre_trabajo = input(f"Ingrese el nombre del trabajo {i+1}: ")
    trabajo = Trabajo(nombre_trabajo)
    trabajos.append(trabajo)

# Asignar trabajos a personas
for persona in personas:
    print(f"Para {persona.nombre}, elija un trabajo:")
    for i, trabajo in enumerate(trabajos):
        print(f"{i + 1}. {trabajo.nombre}")

    opcion = int(input("Elija el número correspondiente al trabajo: ")) - 1
    trabajador = Trabajador(persona, trabajos[opcion])
    persona.trabajo = trabajador

# Mostrar la relación entre persona, trabajo y trabajador
for persona in personas:
    print(f"{persona.nombre} trabaja en {persona.trabajo.trabajo.nombre}")
