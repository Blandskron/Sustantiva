def count_letters(phrase):
    # Inicializa un diccionario para almacenar las ocurrencias de cada caracter.
    characters = {}

    # Itera sobre cada caracter en la frase.
    for character in phrase:
        # Verifica si el caracter ya está en el diccionario.
        if character in characters:
            # Si el caracter ya existe, incrementa su conteo en 1.
            characters[character] += 1
        else:
            # Si el caracter no existe, lo agrega al diccionario con un conteo inicial de 1.
            characters[character] = 1

    # Retorna el diccionario con el conteo de caracteres.
    return characters

# Llama a la función count_letters con una frase como argumento.
response = count_letters("Lorem ipsum dolor sit amet, consecetur adipiscing eit. Sed euismod mollis est, at dictum lectus auctor vel. Vivamus sit amet sem massa.")

# Imprime el resultado del conteo de letras.
print(response)
