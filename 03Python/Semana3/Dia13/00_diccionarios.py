# Definición de un diccionario de estudiantes
estudiantes = {
    "Juan": 18,
    "María": 20,
    "Carlos": 19
}

# Acceso e impresión de los datos del diccionario
print("Edad de Juan:", estudiantes["Juan"])
print("Edad de María:", estudiantes.get("María"))

# Agregar un nuevo estudiante al diccionario
estudiantes["Ana"] = 21
print("Diccionario después de agregar a Ana:", estudiantes)

# Eliminar un estudiante del diccionario
del estudiantes["Carlos"]
print("Diccionario después de eliminar a Carlos:", estudiantes)
