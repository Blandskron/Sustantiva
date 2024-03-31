# Creamos un diccionario llamado 'empleados' donde las claves son los identificadores de los empleados
# y los valores son diccionarios que contienen información sobre cada empleado.
empleados = {
    '001': {'nombre': 'Juan', 'edad': 30, 'puesto': 'ingeniero'},
    '002': {'nombre': 'María', 'edad': 35, 'puesto': 'analista'},
    '003': {'nombre': 'Carlos', 'edad': 28, 'puesto': 'gerente'}
}

# Obtener la información de un empleado específico (en este caso, el empleado con el identificador '001')
print("La información del empleado 001 es:", empleados['001'])

# Cambiar el puesto de un empleado (cambiamos el puesto de María)
empleados['002']['puesto'] = 'gerente de proyecto'
print("La información actualizada de María es:", empleados['002'])

# Eliminar a un empleado (eliminamos a Carlos del diccionario de empleados)
del empleados['003']
print("Después de eliminar a Carlos, los empleados restantes son:", empleados)
