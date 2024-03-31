def coin_change_greedy(coins, amount):
    n = len(coins)
    result = []

    for i in range(n-1, -1, -1):
        while amount >= coins[i]:
            amount -= coins[i]
            result.append(coins[i])
            print(f"Agregando moneda de {coins[i]} al cambio. Cantidad restante: {amount}")

    return result

# Ejemplo de uso
coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
amount = 867
change = coin_change_greedy(coins, amount)
print("\nCambio proporcionado:", change)

