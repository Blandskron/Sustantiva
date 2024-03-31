class ManejoDatos:
    def __init__(self):
        try:
            lista = [1, 2, 3]
            print("Elemento en el índice 5:", lista[5])  # Genera una excepción IndexError

            diccionario = {'a': 1, 'b': 2}
            print("Valor de la clave 'c':", diccionario['c'])  # Genera una excepción KeyError

            objeto = object()
            print("Atributo del objeto:", objeto.atributo)  # Genera una excepción AttributeError
        except IndexError:
            print("Error: Índice fuera de rango.")
        except KeyError:
            print("Error: Clave no encontrada en el diccionario.")
        except AttributeError:
            print("Error: Atributo no encontrado en el objeto.")

# Ejemplo de uso
manejo_datos = ManejoDatos()
