# Definición de una cadena de caracteres
cadena = 'Python'

# Iteración sobre cada letra en la cadena 'cadena'
for letra in cadena:
    # Verifica si la letra actual es 'h'
    if letra == 'h':
        # Si encuentra la letra 'h', imprime un mensaje y sale del bucle
        print("Se encontro la h")
        break
    # Si la letra no es 'h', imprime la letra
    print(letra)
