def truth_table():
    headers = ["p", "q", "p AND q", "p OR q", "NOT p"]
    print("|", "|".join(headers), "|")

    for p in [True, False]:
        for q in [True, False]:
            p_and_q = p and q
            p_or_q = p or q
            not_p = not p
            row = [str(int(p)), str(int(q)), str(int(p_and_q)), str(int(p_or_q)), str(int(not_p))]
            print("|", "|".join(row), "|")

# Llamar a la función para imprimir la tabla de verdad
truth_table()

def truth_table():
    headers = ["p", "q", "p AND q", "p OR q", "NOT p"]
    print("|", "|".join(headers), "|")

    for p in [True, False]:
        for q in [True, False]:
            p_and_q = p and q
            p_or_q = p or q
            not_p = not p
            row = [str(p), str(q), str(p_and_q), str(p_or_q), str(not_p)]
            print("|", "|".join(row), "|")

# Llamar a la función para imprimir la tabla de verdad
truth_table()

def print_truth_values(p, q):
    print(f"p = {p}, q = {q}")
    print(f"p AND q = {p and q}")
    print(f"p OR q  = {p or q}")
    print(f"NOT p   = {not p}")
    print("-----------------------")

# Combinaciones de valores booleanos para p y q
boolean_values = [True, False]

# Generar y mostrar la tabla de verdad
for p in boolean_values:
    for q in boolean_values:
        print_truth_values(p, q)
