class TraductorUniversal:
    def __init__(self, idioma_fuente, idioma_destino):
        """
        Constructor de la clase TraductorUniversal.

        Args:
        - idioma_fuente (str): El idioma del mensaje de origen.
        - idioma_destino (str): El idioma al que se traduce el mensaje.
        """
        self.idioma_fuente = idioma_fuente        # Asigna el idioma fuente al atributo 'idioma_fuente'
        self.idioma_destino = idioma_destino      # Asigna el idioma destino al atributo 'idioma_destino'

    def traducir(self, mensaje):
        """
        Método para traducir un mensaje del idioma fuente al idioma destino.

        Args:
        - mensaje (str): El mensaje que se va a traducir.
        """
        print(f"Traduciendo del idioma {self.idioma_fuente} al {self.idioma_destino}: {mensaje}")

# Crear una instancia de TraductorUniversal
traductor_marciano = TraductorUniversal("Marciano", "Inglés")  # Crea una instancia de TraductorUniversal con idioma fuente "Marciano" y idioma destino "Inglés"

# Llamar al método traducir() para traducir un mensaje
traductor_marciano.traducir("Saludos desde Marte.")  # Traduce el mensaje "Saludos desde Marte." del idioma Marciano al Inglés
