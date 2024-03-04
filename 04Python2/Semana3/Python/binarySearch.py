def binary_search_verbose(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        print(f"Revisando el rango {arr[low:high+1]}, punto medio en índice {mid}, valor {arr[mid]}")

        # Verificar si x está presente en el medio
        if arr[mid] == x:
            return mid

        # Si x es mayor, ignorar la mitad izquierda
        elif arr[mid] < x:
            low = mid + 1

        # Si x es menor, ignorar la mitad derecha
        else:
            high = mid - 1

    # Si el elemento no está presente en el array
    return -1

# Ejemplo de uso
example_array = [2, 3, 4, 10, 40]
x = 10
result = binary_search_verbose(example_array, 0, len(example_array)-1, x)

if result != -1:
    print(f"Elemento encontrado en el índice {result}")
else:
    print("Elemento no presente en el array")

