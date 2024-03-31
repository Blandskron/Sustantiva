def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # crear arrays temporales
    L = [0] * n1
    R = [0] * n2

    # Copiar datos a los arrays temporales L[] y R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Fusionar los arrays temporales de vuelta al array arr[l..r]
    i = 0     # Índice inicial del primer subarray
    j = 0     # Índice inicial del segundo subarray
    k = l     # Índice inicial del subarray fusionado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si hay alguno
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si hay alguno
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_verbose(arr, l, r):
    if l < r:
        # Igual que (l+r)//2, pero evita desbordamiento para grandes l y h
        m = l + (r - l) // 2

        # Ordenar la primera y segunda mitad
        merge_sort_verbose(arr, l, m)
        merge_sort_verbose(arr, m+1, r)
        merge(arr, l, m, r)

        print(f"Uniendo subarrays: {arr[l:r+1]}")

# Ejemplo de uso
example_array = [12, 11, 13, 5, 6]
n = len(example_array)
merge_sort_verbose(example_array, 0, n-1)
print("Array ordenado:", example_array)

