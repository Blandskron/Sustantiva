def insertion_sort_verbose(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        print(f"Paso {i}:")
        print("Array antes de las inserciones:", arr)
        # Mover los elementos de arr[0..i-1], que son
        # mayores que key, a una posición adelante
        # de su posición actual
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print("Array después de las inserciones:", arr)
        print("")

    return arr

# Ejemplo de uso
example_array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort_verbose(example_array)
print("Array ordenado:", sorted_array)

