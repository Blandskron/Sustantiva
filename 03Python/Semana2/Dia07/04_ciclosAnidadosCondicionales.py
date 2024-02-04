grupo1 = [5, 13, 16, 7]
grupo2 = [5, 14, 15, 20]
for numero1 in grupo1:
    for numero2 in grupo2:
        if numero1 == numero2:
            continue
        elif numero1 > numero2:
            break
        else:
            print("Conclusion: ", numero1, "es menor que ", numero2)