# Definición de la función find_words_with_two_vowels() que encuentra palabras con exactamente dos vocales
def find_words_with_two_vowels(words):
    # Conjunto de vocales en mayúsculas y minúsculas
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Retorna una lista de palabras que tienen exactamente dos vocales
    return [word for word in words if sum(1 for char in word if char in vowels) == 2]

# Llamada a la función find_words_with_two_vowels() con una lista de palabras
response = find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "sustantiva"
])

# Imprime la lista de palabras que contienen exactamente dos vocales
print(response)

"""
Comentarios detallados:

def find_words_with_two_vowels(words):: Define una función llamada find_words_with_two_vowels() que toma una lista de palabras como entrada.

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}: Define un conjunto de vocales, tanto en minúsculas como en mayúsculas.

La comprensión de lista [word for word in words if sum(1 for char in word if char in vowels) == 2] itera sobre cada palabra en la lista words y verifica si la cantidad de vocales en esa palabra es igual a 2.

for word in words: Itera sobre cada palabra en la lista words.
for char in word if char in vowels: Itera sobre cada caracter en la palabra word que está en el conjunto de vocales vowels.
sum(1 for char in word if char in vowels) == 2: Suma 1 por cada vocal en la palabra word y verifica si el total es igual a 2.
Si el total es igual a 2, la palabra se incluye en la lista resultante.
response almacenará la lista de palabras que contienen exactamente dos vocales.

print(response): Imprime la lista de palabras que contienen exactamente dos vocales.
"""