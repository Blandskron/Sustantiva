try:
    # Código que utiliza muchos recursos de memoria
    lista_grande = [i for i in range(1000000)]
    print("Operaciones realizadas con la lista grande...")
except Exception as e:
    print("Ocurrió un error:", e)
finally:
    del lista_grande
    print("Recursos de memoria liberados.")
