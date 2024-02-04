llueve = True  # Variable booleana que indica si está lloviendo o no
temperatura = int(input("Ingrese temp: "))  # Solicita al usuario ingresar la temperatura

if temperatura < 18 and llueve == True:  # Comprueba si la temperatura es menor que 18 y está lloviendo
    print("Llevaré paraguas y abrigo")  # Si se cumple la condición, imprime que llevará paraguas y abrigo
elif temperatura < 18 and llueve == False:  # Comprueba si la temperatura es menor que 18 y no está lloviendo
    print("Solo llevaré abrigo")  # Si se cumple la condición, imprime que solo llevará abrigo
else:  # Si ninguna de las condiciones anteriores se cumple
    print("No llevaré paraguas ni abrigo")  # Imprime que no llevará paraguas ni abrigo
