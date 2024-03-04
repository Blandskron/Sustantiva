def bubble_sort_verbose(arr):
    n = len(arr)
    for i in range(n):
        print(f"Paso {i + 1}:")
        print("Array actual:", arr)
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Intercambiar elementos en las posiciones {j} y {j+1}: {arr}")
        print("")

    return arr

# Ejemplo de uso
example_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort_verbose(example_array)
print("Array ordenado:", sorted_array)
