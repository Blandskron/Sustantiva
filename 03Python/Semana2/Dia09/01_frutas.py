# Definir una lista de nombres de frutas
frutas = ["manzana", "banana", "naranja", "piña", "uva"]

# Leer la lista
print("Las frutas disponibles son:")
for fruta in frutas:
    print(fruta)

# Consumir la lista
# Verificar si una fruta específica está en la lista
fruta_buscada = "manzana"
if fruta_buscada in frutas:
    print(f"{fruta_buscada} está en la lista de frutas.")
else:
    print(f"{fruta_buscada} no está en la lista de frutas.")
