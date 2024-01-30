def adivinar_sombrero(sombreros):
    adivinaciones = []  # Lista para almacenar las adivinaciones
    
    for i, sombrero in enumerate(sombreros):
        cantidad_azules = sombreros.count('azul')
        
        # Si el número de sombreros azules es par, el último sombrero es azul
        adivinacion = 'azul' if cantidad_azules % 2 == 0 else 'rojo'
        
        # Agregar la adivinación a la lista
        adivinaciones.append(adivinacion)
        
        # Mostrar la adivinación de cada persona
        print(f"Persona {i + 1} adivina: {adivinacion}")
    
    return adivinaciones

# Prueba del algoritmo
sombreros = ['rojo', 'azul', 'rojo']  # Ejemplo de colores de sombreros
adivinaciones = adivinar_sombrero(sombreros)

# Comprobar si al menos una adivinación es correcta
for i, adivinacion in enumerate(adivinaciones):
    if adivinacion == sombreros[i]:
        print(f"Persona {i + 1} ha adivinado correctamente su sombrero.")
        break
