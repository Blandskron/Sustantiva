class GradoEstudio:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    class Detalles:
        def __init__(self, duracion, modalidad):
            self.duracion = duracion
            self.modalidad = modalidad

# Ejemplo de uso
licenciatura = GradoEstudio("Licenciatura en Informática", "Universitario")
licenciatura_detalles = licenciatura.Detalles("4 años", "Presencial")
print(f"Grado de estudio: {licenciatura.nombre}, Nivel: {licenciatura.nivel}")
print(f"Duración: {licenciatura_detalles.duracion}, Modalidad: {licenciatura_detalles.modalidad}")
