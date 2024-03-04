def calcular_imc(peso, altura_en_metros):
    return peso / (altura_en_metros ** 2)

def main():
    print("Calculadora de IMC")

    try:
        peso = float(input("Introduce tu peso en kilogramos: "))
        altura = float(input("Introduce tu altura en centímetros: ")) / 100  # Convertir de cm a metros

        imc = calcular_imc(peso, altura)

        print(f"Tu Índice de Masa Corporal es: {imc:.2f}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()
