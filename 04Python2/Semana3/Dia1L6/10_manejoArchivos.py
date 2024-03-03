class RegistroNotas:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_notas(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                return lineas
        except FileNotFoundError:
            print(f"El archivo '{self.nombre_archivo}' no se ha encontrado.")
            return []

    def calcular_promedios(self, lineas):
        promedios = []
        for linea in lineas:
            datos = linea.strip().split(',')
            nombre = datos[0]
            notas = [int(nota) for nota in datos[1:]]
            promedio = sum(notas) / len(notas)
            promedios.append((nombre, promedio))
        return promedios

    def escribir_promedios(self, promedios):
        try:
            with open('promedios.txt', 'w') as archivo:
                for nombre, promedio in promedios:
                    archivo.write(f"{nombre}: {promedio:.2f}\n")
            print("Los promedios han sido guardados en el archivo 'promedios.txt'.")
        except Exception as e:
            print("Error al escribir en el archivo:", e)


def main():
    registro = RegistroNotas('notas.txt')
    lineas = registro.leer_notas()
    if lineas:
        promedios = registro.calcular_promedios(lineas)
        registro.escribir_promedios(promedios)


if __name__ == "__main__":
    main()
