from datetime import datetime

def calcular_diferencia_fecha(fecha1, fecha2):
    diferencia = fecha2 - fecha1
    return diferencia.days

def main():
    fecha1_input = input("Introduce la primera fecha (formato YYYY-MM-DD): ")
    fecha2_input = input("Introduce la segunda fecha (formato YYYY-MM-DD): ")

    fecha1 = datetime.strptime(fecha1_input, '%Y-%m-%d')
    fecha2 = datetime.strptime(fecha2_input, '%Y-%m-%d')

    if fecha1 > fecha2:
        fecha1, fecha2 = fecha2, fecha1  # Asegura que la fecha1 es la más antigua

    diferencia = calcular_diferencia_fecha(fecha1, fecha2)
    print(f"La diferencia entre las fechas es de {diferencia} días.")

if __name__ == "__main__":
    main()
