# Importar el módulo 'unittest' para escribir y ejecutar pruebas unitarias
import unittest

# Importar la clase 'datetime' del módulo 'datetime' para trabajar con fechas y horas
from datetime import datetime

# Importar la función 'freeze_time' de la biblioteca 'freezegun' para congelar la fecha y hora actuales durante las pruebas
from freezegun import freeze_time

# Definir una función llamada 'finalizar_pandemia' que determina si la pandemia ha finalizado basándose en el año actual
def finalizar_pandemia():
    # Obtener la fecha y hora actuales
    hoy = datetime.today()
    # Verificar si el año actual es mayor que 2022
    if hoy.year > 2022:
        return True
    else:
        return False

# Definir una clase 'Test' que hereda de 'unittest.TestCase' para escribir pruebas unitarias
class Test(unittest.TestCase):

    # Decorador 'freeze_time' utilizado para congelar la fecha y hora actuales durante la ejecución de la prueba
    @freeze_time("2023-01-01")
    # Método de prueba para verificar si 'finalizar_pandemia()' devuelve 'True' cuando se congela el tiempo en "2023-01-01"
    def test_finalizar_pandemia_true(self):
        # Imprimir la fecha y hora actuales para verificar si se ha congelado correctamente el tiempo
        print(datetime.today())
        # Verificar si 'finalizar_pandemia()' devuelve 'True'
        self.assertTrue(finalizar_pandemia())

    # Decorador 'freeze_time' utilizado para congelar la fecha y hora actuales durante la ejecución de la prueba
    @freeze_time("2021-01-01")
    # Método de prueba para verificar si 'finalizar_pandemia()' devuelve 'False' cuando se congela el tiempo en "2021-01-01"
    def test_finalizar_pandemia_false(self):
        # Verificar si 'finalizar_pandemia()' devuelve 'False'
        self.assertFalse(finalizar_pandemia())

# Entrada principal del programa
if __name__ == '__main__':
    # Ejecutar todas las pruebas definidas en la clase 'Test'
    unittest.main()
