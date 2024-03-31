# Definición de la función truth_table() para imprimir una tabla de verdad
def truth_table():
    # Encabezados de la tabla de verdad
    headers = ["p", "q", "p AND q", "p OR q", "NOT p"]
    print("|", "|".join(headers), "|")  # Imprime los encabezados de la tabla

    # Bucle para generar todas las combinaciones de valores booleanos para p y q
    for p in [True, False]:
        for q in [True, False]:
            # Operaciones booleanas para cada combinación de valores de p y q
            p_and_q = p and q
            p_or_q = p or q
            not_p = not p
            
            # Crear una fila de la tabla como una lista de cadenas de texto
            row = [str(int(p)), str(int(q)), str(int(p_and_q)), str(int(p_or_q)), str(int(not_p))]
            
            # Imprimir la fila de la tabla
            print("|", "|".join(row), "|")

# Llamar a la función para imprimir la tabla de verdad
truth_table()


# Definición de la función print_truth_values() para mostrar las operaciones booleanas entre dos valores booleanos p y q
def print_truth_values(p, q):
    # Mostrar los valores de p y q
    print(f"p = {p}, q = {q}")
    # Mostrar el resultado de las operaciones booleanas entre p y q
    print(f"p AND q = {p and q}")
    print(f"p OR q  = {p or q}")
    print(f"NOT p   = {not p}")
    print("-----------------------")

# Combinaciones de valores booleanos para p y q
boolean_values = [True, False]

# Generar y mostrar la tabla de verdad usando la función print_truth_values()
for p in boolean_values:
    for q in boolean_values:
        print_truth_values(p, q)
