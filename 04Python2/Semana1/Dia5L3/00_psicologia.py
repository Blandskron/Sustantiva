class Psicologia:
    def __init__(self, enfoque):
        self.enfoque = enfoque  # Inicialización del atributo enfoque

    def estudiar_comportamiento(self):
        # Método estudiar_comportamiento: Imprime un mensaje sobre el estudio del comportamiento humano
        print(f"Estudiando el comportamiento humano desde el enfoque de {self.enfoque}.")

# Creación de una instancia de la clase Psicologia
psicologia = Psicologia("psicoanálisis")

# Llamada al método para estudiar el comportamiento desde un enfoque específico
psicologia.estudiar_comportamiento()
