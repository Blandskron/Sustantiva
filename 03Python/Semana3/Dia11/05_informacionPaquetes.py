# Definición de una función llamada get_packages_info que procesa información sobre paquetes.
# Toma un argumento:
# - packages: una lista de tuplas, donde cada tupla contiene información sobre un paquete (id, peso, destino).
def get_packages_info(packages):
    # Inicialización de un diccionario para almacenar la información sobre los paquetes.
    rta = {
        "total_weight": 0,   # Peso total de todos los paquetes
        "destinations": {}   # Diccionario para contar la cantidad de paquetes por destino
    }
   
    # Iteración sobre cada paquete en la lista 'packages'
    for package in packages:
        # Extracción del peso y el destino del paquete actual
        weight = package[1]
        destination = package[2]
        
        # Verificación si el destino ya existe en el diccionario 'destinations'
        existDestination = rta["destinations"].get(destination)
        
        # Actualización del peso total sumando el peso del paquete actual
        rta["total_weight"] += weight
        
        # Verificación y actualización del diccionario 'destinations' para contar la cantidad de paquetes por destino
        if existDestination is None:
            rta["destinations"][destination] = 1  # Si el destino no existe, se inicializa en 1
        else:
            rta["destinations"][destination] += 1  # Si el destino ya existe, se incrementa en 1
   
    # Redondeo del peso total a dos decimales
    rta["total_weight"] = round(rta["total_weight"], 2)
   
    # Devuelve el diccionario 'rta' con la información procesada sobre los paquetes.
    return rta
      
# Llama a la función get_packages_info con una lista de paquetes, cada paquete representado por una tupla.
# La función devuelve un diccionario con información procesada sobre los paquetes.
response = get_packages_info([
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
])

# Imprime el diccionario con la información procesada sobre los paquetes.
print(response)
