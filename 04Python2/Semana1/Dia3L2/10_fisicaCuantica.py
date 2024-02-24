class Cuantica:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    class Particula:
        def __init__(self, nombre_particula, carga, spin):
            self.nombre_particula = nombre_particula
            self.carga = carga
            self.spin = spin

    class Experimento:
        def __init__(self, nombre_experimento, descripcion):
            self.nombre_experimento = nombre_experimento
            self.descripcion = descripcion

    class Fenomeno:
        def __init__(self, nombre_fenomeno, descripcion_fenomeno):
            self.nombre_fenomeno = nombre_fenomeno
            self.descripcion_fenomeno = descripcion_fenomeno

    class Teoria:
        def __init__(self, nombre_teoria, ecuaciones):
            self.nombre_teoria = nombre_teoria
            self.ecuaciones = ecuaciones

    class Aplicacion:
        def __init__(self, nombre_aplicacion, campo_aplicacion):
            self.nombre_aplicacion = nombre_aplicacion
            self.campo_aplicacion = campo_aplicacion

# Ejemplo de uso
cuantica = Cuantica("Física Cuántica", "Ciencia")
electron = cuantica.Particula("Electrón", "-e", "1/2")
experimento = cuantica.Experimento("Doble rendija", "Interferencia cuántica")
fenomeno = cuantica.Fenomeno("Entrelazamiento cuántico", "Conexión instantánea entre partículas")
teoria = cuantica.Teoria("Mecánica Cuántica", "Ecuación de Schrödinger")
aplicacion = cuantica.Aplicacion("Computación Cuántica", "Criptografía y simulaciones cuánticas")

print(f"Nombre: {cuantica.nombre}, Tipo: {cuantica.tipo}")
print(f"Partícula: {electron.nombre_particula}, Carga: {electron.carga}, Spin: {electron.spin}")
print(f"Experimento: {experimento.nombre_experimento}, Descripción: {experimento.descripcion}")
print(f"Fenómeno: {fenomeno.nombre_fenomeno}, Descripción: {fenomeno.descripcion_fenomeno}")
print(f"Teoría: {teoria.nombre_teoria}, Ecuaciones: {teoria.ecuaciones}")
print(f"Aplicación: {aplicacion.nombre_aplicacion}, Campo: {aplicacion.campo_aplicacion}")
