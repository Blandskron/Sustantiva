# Lista de tareas domésticas
tareas_domesticas = ["Lavar platos", "Barrer", "Hacer la cama", "Lavar la ropa"]

# Imprime un encabezado para indicar que se mostrará la distribución de tareas domésticas
print("Distribución de tareas domésticas:")

# Itera sobre la lista de tareas domésticas utilizando la función enumerate()
# La función enumerate() devuelve tanto el índice como el elemento de la lista en cada iteración
# El parámetro start=1 indica que los índices comienzan desde 1 en lugar de 0
for i, tarea in enumerate(tareas_domesticas, start=1):
    # Imprime el número de semana (índice + 1) y la tarea doméstica correspondiente
    # Se utiliza una f-string para formatear el mensaje de manera clara y legible
    print(f"Semana {i}: {tarea}")
