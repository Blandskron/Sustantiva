# Definir una lista de coordenadas (tuplas)
coordenadas = [(0, 0), (1, 2), (3, 4), (5, 6)]

# Leer la lista
print("Las coordenadas son:")
for coordenada in coordenadas:
    print(coordenada)

# Consumir la lista
# Calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

punto1 = (0, 0)
punto2 = (3, 4)
distancia = distancia_euclidiana(punto1, punto2)
print("La distancia entre los puntos", punto1, "y", punto2, "es:", distancia)
