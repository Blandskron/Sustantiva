# Importar la función de saludo desde el módulo saludo
from modulos import saludo

# Importar la función de despedida desde el submódulo despedida del paquete modulos
from modulos.despedida import despedida

# Definir la función principal del programa
def main():
    # Solicitar al usuario su nombre
    nombre = input("Por favor, introduce tu nombre: ")
    
    # Llamar a la función de saludo del módulo saludo con el nombre proporcionado
    saludo.saludar(nombre)
    
    # Llamar a la función de despedida del submódulo despedida con el nombre proporcionado
    despedida.despedirse(nombre)

# Verificar si este script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Si es así, llamar a la función principal
    main()
