# Importar el módulo de saludos
import saludos

def main():
    # Solicitar al usuario su nombre
    nombre = input("Por favor, introduce tu nombre: ")
    
    # Llamar a la función de saludo del módulo con el nombre proporcionado
    saludos.saludar(nombre)

if __name__ == "__main__":
    main()
