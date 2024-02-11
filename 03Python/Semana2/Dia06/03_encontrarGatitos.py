# Definición de una función llamada find_famous_cat que encuentra al gato(s) más famoso(s) basado en el número total de seguidores.
# Toma un argumento:
# - cats: una lista de diccionarios, donde cada diccionario representa un gato con su nombre y la cantidad de seguidores.
def find_famous_cat(cats):
    # Inicialización de un diccionario para almacenar la información sobre el gato más famoso.
    famous_stats = {
        "famous_cats": [],  # Lista de nombres de gatos más famosos
        "max_followers": 0  # Número máximo de seguidores entre los gatos
    }
  
    # Iteración sobre cada gato en la lista 'cats'
    for cat in cats:
        total_followers = 0  # Inicialización del contador de seguidores para cada gato
        # Iteración sobre la lista de seguidores del gato actual
        for num in cat["followers"]:
            total_followers += num  # Suma de los seguidores del gato actual
      
        # Comprobación si el total de seguidores del gato actual es mayor que el máximo registrado
        if total_followers > famous_stats["max_followers"]:
            # Si es así, actualiza el máximo de seguidores y reinicia la lista de gatos famosos
            famous_stats["max_followers"] = total_followers
            famous_stats["famous_cats"] = []  # Reinicia la lista de gatos famosos
            famous_stats["famous_cats"].append(cat["name"])  # Agrega el nombre del gato actual a la lista
        # Si el total de seguidores es igual al máximo registrado, agrega el nombre del gato actual a la lista de famosos
        elif total_followers == famous_stats["max_followers"]:
            famous_stats["famous_cats"].append(cat["name"])
  
    # Devuelve la lista de nombres de los gatos más famosos.
    return famous_stats["famous_cats"]

# Llama a la función find_famous_cat con una lista de gatos, cada gato representado por un diccionario.
# La función devuelve una lista de nombres de los gatos más famosos.
response = find_famous_cat([
    {
        "name": "Luna",
        "followers": [500, 200, 300]
    },
    {
        "name": "Michi",
        "followers": [100, 500]
    }
])

# Imprime la lista de nombres de los gatos más famosos.
print(response)
