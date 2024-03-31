llueve = True  # Variable booleana que indica si está lloviendo o no
temperatura = int(input("Ingresa temp: "))  # Solicita al usuario ingresar la temperatura

if temperatura < 18:  # Comprueba si la temperatura es menor que 18
    if llueve == True:  # Si la temperatura es menor que 18, comprueba si está lloviendo
        print("Llevaré paraguas y abrigo")  # Si llueve, imprime que llevará paraguas y abrigo
    else:  # Si no llueve
        print("Solo llevaré abrigo")  # Imprime que solo llevará abrigo
else:  # Si la temperatura es mayor o igual que 18
    print("No necesito paraguas ni abrigo")  # Imprime que no necesita paraguas ni abrigo
