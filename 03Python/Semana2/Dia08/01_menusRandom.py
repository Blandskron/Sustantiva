# Importa el módulo random para generar números aleatorios y seleccionar elementos de la lista
import random

# Lista de platos disponibles para el menú
platos = ["Pollo asado", "Pasta al pesto", "Ensalada César", "Sushi", "Tacos"]

# Itera sobre cada día de la semana
for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
    # Selecciona aleatoriamente un plato de la lista 'platos' para el día actual y lo imprime
    print(f"Menú para {dia}: {random.choice(platos)}")
