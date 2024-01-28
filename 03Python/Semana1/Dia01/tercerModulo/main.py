from modulos import saludo
from modulos.despedida import despedida

def main():
    nombre = input("Por favor, introduce tu nombre: ")
    
    # Llamar a la función de saludo del módulo saludo
    saludo.saludar(nombre)
    
    # Llamar a la función de despedida del módulo despedida
    despedida.despedirse(nombre)

if __name__ == "__main__":
    main()
