def es_seguro(tablero, fila, columna, N):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar si hay una reina en la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar si hay una reina en la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, fila, N):
    # Si todas las reinas están colocadas, retornar verdadero
    if fila >= N:
        return True

    # Considerar esta fila y probar colocar una reina en todas las columnas una por una
    for i in range(N):
        if es_seguro(tablero, fila, i, N):
            tablero[fila][i] = 1  # Colocar la reina

            # Recurso para colocar el resto de las reinas
            if resolver_n_reinas(tablero, fila + 1, N):
                return True

            tablero[fila][i] = 0  # Si colocar reina en tablero[fila][i] no conduce a una solución, remover reina

    # Si la reina no puede ser colocada en ninguna fila en esta columna, retornar falso
    return False

def imprimir_solucion(tablero, N):
    for i in range(N):
        for j in range(N):
            print(tablero[i][j], end=" ")
        print()

# Función principal para resolver el problema de las N-Reinas
def n_reinas(N):
    tablero = [[0 for _ in range(N)] for _ in range(N)]

    if not resolver_n_reinas(tablero, 0, N):
        print("No existe una solución para el problema de las N-Reinas con N =", N)
    else:
        imprimir_solucion(tablero, N)

# Probemos el algoritmo con un tablero de 4x4
n_reinas(4)
