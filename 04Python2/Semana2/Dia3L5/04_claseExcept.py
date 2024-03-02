class Estudiante:
    def __init__(self, nombre, edad, grado):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        if not isinstance(grado, int):
            raise TypeError("El grado debe ser un número entero.")

        if edad < 0:
            raise ValueError("La edad no puede ser un número negativo.")
        if grado <= 0:
            raise ValueError("El grado debe ser un número positivo mayor que cero.")

        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estoy en {self.grado} grado.")

# Ejemplo de uso con manejo de excepciones
try:
    estudiante1 = Estudiante("Maria", 15, "9")  # Aquí se genera una excepción TypeError
except TypeError as e:
    print("Error al crear estudiante:", e)

try:
    estudiante2 = Estudiante("Juan", -5, 8)  # Aquí se genera una excepción ValueError
except ValueError as e:
    print("Error al crear estudiante:", e)

try:
    estudiante3 = Estudiante(123, 15, 9)  # Aquí se genera una excepción TypeError
except TypeError as e:
    print("Error al crear estudiante:", e)
