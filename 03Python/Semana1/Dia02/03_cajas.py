def determinar_contenido(caja_a):
    if caja_a == "tornillos":
        contenido_caja_a = "Tornillos"
        contenido_caja_b = "Tuercas"
        contenido_caja_c = "Tornillos y Tuercas"
    elif caja_a == "tuercas":
        contenido_caja_a = "Tuercas"
        contenido_caja_b = "Tornillos"
        contenido_caja_c = "Tornillos y Tuercas"
    elif caja_a == "tornillos y tuercas":
        contenido_caja_a = "Tornillos y Tuercas"
        contenido_caja_b = "Tornillos"
        contenido_caja_c = "Tuercas"
    else:
        contenido_caja_a = "Error"
        contenido_caja_b = "Error"
        contenido_caja_c = "Error"
    
    return contenido_caja_a, contenido_caja_b, contenido_caja_c

# Prueba del algoritmo
caja_a = input("Ingresa el contenido de la Caja A (tornillos, tuercas, tornillos y tuercas): ").lower()

contenido_caja_a, contenido_caja_b, contenido_caja_c = determinar_contenido(caja_a)

print("Contenido de la Caja A:", contenido_caja_a)
print("Contenido de la Caja B:", contenido_caja_b)
print("Contenido de la Caja C:", contenido_caja_c)
