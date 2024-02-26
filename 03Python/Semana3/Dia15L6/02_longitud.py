# Definición de la función count_words_by_length() que cuenta las palabras por longitud
def count_words_by_length(words):
    # Retorna un diccionario donde las claves son las longitudes de las palabras
    # y los valores son el número de palabras con esa longitud
    return {len(word): sum(1 for w in words if len(w) == len(word)) for word in words}

# Llamada a la función count_words_by_length() con una lista de palabras
response = count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

# Imprime el diccionario que contiene la cuenta de palabras por longitud
print(response)
