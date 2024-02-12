def saludar(nombre, mensaje="Hola", emoticon="😊"):
    print(f"{mensaje}, {nombre} {emoticon}")

saludar("Ana")  # Salida: Hola, Ana 😊
saludar("Pedro", emoticon="👋")  # Salida: Hola, Pedro 👋
saludar(mensaje="Hola", nombre="Sofía")  # Salida: Hola, Sofía 😊
