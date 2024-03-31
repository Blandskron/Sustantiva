import psycopg2

try:
    conexion = psycopg2.connect(user="usuario", password="contraseña", host="localhost", port="5432", database="basedatos")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tabla")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
except psycopg2.Error as error:
    print("Error al conectarse a la base de datos:", error)
finally:
    if 'conexion' in locals():
        conexion.close()
