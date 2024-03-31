# Creamos un conjunto llamado "invitados" con nombres de personas.
invitados = {"Luis", "Ana", "Sebastián", "Sofía", "Mateo", "Ana", "Sebastián"}

# Imprimimos el conjunto de invitados.
print("Lista de invitados:", invitados)

# No podemos acceder a elementos individuales de un conjunto por índice,
# ya que los conjuntos son colecciones desordenadas y no admiten indexación.

# Iteramos sobre cada elemento en el conjunto "invitados" e imprimimos el nombre de cada invitado.
for invitado in invitados:
    print(f"Nombre de invitado(a): {invitado}")
