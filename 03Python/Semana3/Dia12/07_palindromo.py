def find_largest_palindrome(words):
    largest_palindrome = ""  # Inicializa una cadena vacía para almacenar el palíndromo más largo encontrado

    # Itera sobre cada palabra en la lista de palabras
    for word in words:
        reversed_word = ""  # Inicializa una cadena vacía para almacenar la palabra invertida
        
        # Itera sobre los índices de la palabra de forma inversa
        for value in range(len(word), 0, -1):
            letter = word[value - 1]  # Obtiene la letra correspondiente al índice actual
            reversed_word += letter  # Agrega la letra a la palabra invertida
        
        # Si la palabra invertida es igual a la palabra original, es un palíndromo
        if reversed_word == word:
            # Comprueba si la palabra actual es más larga que el palíndromo más largo encontrado hasta ahora
            if len(word) > len(largest_palindrome):
                largest_palindrome = word  # Actualiza la variable del palíndromo más largo
    
    # Si no se encontró ningún palíndromo, devuelve None
    if largest_palindrome == "":
        return None
    
    return largest_palindrome  # Devuelve la palabra palíndromo más larga encontrada

# Llama a la función find_largest_palindrome con una lista de palabras.
response = find_largest_palindrome(["racecar", "level", "world", "hello"])

# Imprime la palabra palíndromo más larga encontrada.
print(response)
