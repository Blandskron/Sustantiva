# Definición de los ingresos mensuales de la familia
ingresos_mensuales = float(input("Ingrese el total de ingresos mensuales: "))

# Creación de un diccionario para almacenar los gastos mensuales
gastos_mensuales = {}

# Solicitar y almacenar los gastos mensuales en diferentes categorías
categorias = ["Alimentación", "Transporte", "Vivienda", "Educación", "Entretenimiento"]

for categoria in categorias:
    gasto = float(input(f"Ingrese el gasto mensual para {categoria}: "))
    gastos_mensuales[categoria] = gasto

# Calcular el total de los gastos mensuales
total_gastos = sum(gastos_mensuales.values())

# Mostrar un resumen de los ingresos y gastos mensuales
print("\nResumen de ingresos y gastos:")
print(f"Ingresos mensuales: ${ingresos_mensuales}")
print(f"Gastos mensuales totales: ${total_gastos}")

# Calcular el saldo restante después de los gastos
saldo_restante = ingresos_mensuales - total_gastos

# Verificar si el saldo es positivo o negativo
if saldo_restante >= 0:
    print(f"\n¡Excelente! Su saldo restante es de ${saldo_restante}.")
else:
    print("\nAdvertencia: ¡Ha excedido su presupuesto mensual!")
    print(f"Su saldo restante es de ${saldo_restante}. Debe revisar sus gastos.")
