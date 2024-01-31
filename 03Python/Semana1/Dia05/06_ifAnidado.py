llueve = True
temperatura = int(input("Ingresa temp: "))
if temperatura < 18:
    if llueve == True:
        print("Llevare paraguas y abrigo")
    else:
        print("Solo llevare abrigo")
else:
    print("No necesito paraguas ni abrigo")