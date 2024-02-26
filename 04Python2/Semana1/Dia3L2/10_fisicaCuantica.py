# Definición de la clase Cuantica
class Cuantica:
    def __init__(self, nombre, tipo):
        # Constructor que inicializa el nombre y el tipo de la física cuántica
        self.nombre = nombre
        self.tipo = tipo

    # Clase interna que representa una partícula cuántica
    class Particula:
        def __init__(self, nombre_particula, carga, spin):
            # Constructor que inicializa el nombre de la partícula, su carga y su spin
            self.nombre_particula = nombre_particula
            self.carga = carga
            self.spin = spin

    # Clase interna que representa un experimento cuántico
    class Experimento:
        def __init__(self, nombre_experimento, descripcion):
            # Constructor que inicializa el nombre del experimento y su descripción
            self.nombre_experimento = nombre_experimento
            self.descripcion = descripcion

    # Clase interna que representa un fenómeno cuántico
    class Fenomeno:
        def __init__(self, nombre_fenomeno, descripcion_fenomeno):
            # Constructor que inicializa el nombre del fenómeno y su descripción
            self.nombre_fenomeno = nombre_fenomeno
            self.descripcion_fenomeno = descripcion_fenomeno

    # Clase interna que representa una teoría cuántica
    class Teoria:
        def __init__(self, nombre_teoria, ecuaciones):
            # Constructor que inicializa el nombre de la teoría y sus ecuaciones asociadas
            self.nombre_teoria = nombre_teoria
            self.ecuaciones = ecuaciones

    # Clase interna que representa una aplicación de la física cuántica
    class Aplicacion:
        def __init__(self, nombre_aplicacion, campo_aplicacion):
            # Constructor que inicializa el nombre de la aplicación y el campo de su aplicación
            self.nombre_aplicacion = nombre_aplicacion
            self.campo_aplicacion = campo_aplicacion

# Ejemplo de uso
# Instanciación de objetos de las clases internas de Cuantica
cuantica = Cuantica("Física Cuántica", "Ciencia")
electron = cuantica.Particula("Electrón", "-e", "1/2")
experimento = cuantica.Experimento("Doble rendija", "Interferencia cuántica")
fenomeno = cuantica.Fenomeno("Entrelazamiento cuántico", "Conexión instantánea entre partículas")
teoria = cuantica.Teoria("Mecánica Cuántica", "Ecuación de Schrödinger")
aplicacion = cuantica.Aplicacion("Computación Cuántica", "Criptografía y simulaciones cuánticas")

# Impresión de la información de los objetos creados
print(f"Nombre: {cuantica.nombre}, Tipo: {cuantica.tipo}")
print(f"Partícula: {electron.nombre_particula}, Carga: {electron.carga}, Spin: {electron.spin}")
print(f"Experimento: {experimento.nombre_experimento}, Descripción: {experimento.descripcion}")
print(f"Fenómeno: {fenomeno.nombre_fenomeno}, Descripción: {fenomeno.descripcion_fenomeno}")
print(f"Teoría: {teoria.nombre_teoria}, Ecuaciones: {teoria.ecuaciones}")
print(f"Aplicación: {aplicacion.nombre_aplicacion}, Campo: {aplicacion.campo_aplicacion}")
