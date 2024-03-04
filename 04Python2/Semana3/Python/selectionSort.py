def selection_sort_verbose(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        print(f"Paso {i + 1}:")
        print("Array actual:", arr)
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Seleccionar mínimo y cambiar:", arr)
        print("")

    return arr

# Ejemplo de uso
example_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort_verbose(example_array)
print("Array ordenado:", sorted_array)

