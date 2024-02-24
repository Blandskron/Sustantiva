import pandas as pd
import sqlite3

# Leer los datos del archivo CSV
datos = pd.read_csv('datos.csv')

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('base_de_datos.db')

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Crear una tabla en la base de datos si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER
                  )''')

# Iterar sobre cada fila del DataFrame y insertar los datos en la base de datos
for index, fila in datos.iterrows():
    nombre = fila['nombre']
    edad = fila['edad']
    cursor.execute('''INSERT INTO personas (nombre, edad) VALUES (?, ?)''', (nombre, edad))

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Los datos se han insertado correctamente en la base de datos.")
