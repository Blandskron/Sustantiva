a = [5, 1, 4, 9, 0]
b = list(range(3, 10)) + list(range(20, 23))
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]

# Expresiones a evaluar
resultado_a2 = a[2]
resultado_b9 = b[9]
resultado_c12 = c[1][2]
resultado_e01_igual = e[0] == e[1]
resultado_len_c = len(c)
resultado_len_c0 = len(c[0])
resultado_len_e = len(e)
resultado_c_ultimo = c[-1]
resultado_c_ultimo_p1 = c[-1][+1]
c[2:] = d[2:]
resultado_a_3_10 = a[3:10]
resultado_a_3_10_2 = a[3:10:2]
resultado_d_jirafa = d.index('jirafa')
resultado_e_c01_count5 = e[c[0][1]].count(5)
resultado_sorted_a2 = sorted(a)[2]
resultado_complex_b0_b1 = complex(b[0], b[1])

# Imprimir resultados y tipos de datos
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
