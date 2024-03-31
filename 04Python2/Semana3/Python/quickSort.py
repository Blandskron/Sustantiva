def partition(arr, low, high):
    # Seleccionar el último elemento como pivote
    pivot = arr[high]
    i = low - 1 # índice del elemento más pequeño

    for j in range(low, high):
        # Si el elemento actual es más pequeño o igual al pivote
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Intercambiar el elemento pivot a su posición correcta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_verbose(arr, low, high):
    if low < high:
        # pi es el índice de partición, arr[pi] está en su lugar
        pi = partition(arr, low, high)

        print(f"Array tras partición en {arr[pi]}: {arr[low:high+1]}")

        # Separar los elementos antes y después de la partición
        quick_sort_verbose(arr, low, pi-1)
        quick_sort_verbose(arr, pi+1, high)

# Ejemplo de uso
example_array = [10, 7, 8, 9, 1, 5]
n = len(example_array)
quick_sort_verbose(example_array, 0, n-1)
print("Array ordenado:", example_array)

