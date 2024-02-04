# Lista a
a = [5, 1, 4, 9, 0]

# Lista b: Concatenación de dos rangos de números
b = list(range(3, 10)) + list(range(20, 23))

# Lista c: Lista de listas
c = [[1, 2], [3, 4, 5], [6, 7]]

# Lista d: Lista de cadenas de texto
d = ['perro', 'gato', 'jirafa', 'elefante']

# Lista e: Contiene una cadena de texto, la lista a, y la lista a repetida dos veces
e = ['a', a, 2 * a]

# Expresiones y evaluaciones
resultado_a2 = a[2]  # Valor en la posición 2 de la lista a
resultado_b9 = b[9]  # Valor en la posición 9 de la lista b
resultado_c12 = c[1][2]  # Valor en la posición 2 de la lista en la posición 1 de la lista c
resultado_e01_igual = e[0] == e[1]  # Compara el primer elemento de e con el segundo
resultado_len_c = len(c)  # Longitud de la lista c
resultado_len_c0 = len(c[0])  # Longitud de la primera lista dentro de c
resultado_len_e = len(e)  # Longitud de la lista e
resultado_c_ultimo = c[-1]  # Última lista en la lista c
resultado_c_ultimo_p1 = c[-1][+1]  # El segundo elemento de la última lista en c
c[2:] = d[2:]  # Asigna las sublistas de d a partir de la posición 2 a la lista c
resultado_a_3_10 = a[3:10]  # Sublista de a desde la posición 3 hasta la 10 (exclusiva)
resultado_a_3_10_2 = a[3:10:2]  # Sublista de a desde la posición 3 hasta la 10 (exclusiva) con un paso de 2
resultado_d_jirafa = d.index('jirafa')  # Índice de 'jirafa' en la lista d
resultado_e_c01_count5 = e[c[0][1]].count(5)  # Cuenta el número de ocurrencias de 5 en la sublista de e en la posición 1 de la lista c
resultado_sorted_a2 = sorted(a)[2]  # El tercer elemento después de ordenar la lista a de forma ascendente
resultado_complex_b0_b1 = complex(b[0], b[1])  # Crea un número complejo usando los dos primeros elementos de b

# Impresión de resultados y tipos de datos
print(f"Resultado a[2]: {resultado_a2}, Tipo: {type(resultado_a2)}")
print(f"Resultado b[9]: {resultado_b9}, Tipo: {type(resultado_b9)}")
print(f"Resultado c[1][2]: {resultado_c12}, Tipo: {type(resultado_c12)}")
print(f"Resultado e[0] == e[1]: {resultado_e01_igual}, Tipo: {type(resultado_e01_igual)}")
print(f"Resultado len(c): {resultado_len_c}, Tipo: {type(resultado_len_c)}")
print(f"Resultado len(c[0]): {resultado_len_c0}, Tipo: {type(resultado_len_c0)}")
print(f"Resultado len(e): {resultado_len_e}, Tipo: {type(resultado_len_e)}")
print(f"Resultado c[-1]: {resultado_c_ultimo}, Tipo: {type(resultado_c_ultimo)}")
print(f"Resultado c[-1][+1]: {resultado_c_ultimo_p1}, Tipo: {type(resultado_c_ultimo_p1)}")
print(f"Resultado c[2:] = d[2:]: {c}, Tipo: {type(c)}")
print(f"Resultado a[3:10]: {resultado_a_3_10}, Tipo: {type(resultado_a_3_10)}")
print(f"Resultado a[3:10:2]: {resultado_a_3_10_2}, Tipo: {type(resultado_a_3_10_2)}")
print(f"Resultado d.index('jirafa'): {resultado_d_jirafa}, Tipo: {type(resultado_d_jirafa)}")
print(f"Resultado e[c[0][1]].count(5): {resultado_e_c01_count5}, Tipo: {type(resultado_e_c01_count5)}")
print(f"Resultado sorted(a)[2]: {resultado_sorted_a2}, Tipo: {type(resultado_sorted_a2)}")
print(f"Resultado complex(b[0], b[1]): {resultado_complex_b0_b1}, Tipo: {type(resultado_complex_b0_b1)}")
