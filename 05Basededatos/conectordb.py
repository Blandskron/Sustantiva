import psycopg2
from psycopg2 import Error

try:
    # Conectarse a la base de datos PostgreSQL
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="test")

    # Crear un cursor para ejecutar operaciones con la base de datos
    cursor = connection.cursor()
    
    # Crear tabla si no existe
    create_table_query = '''CREATE TABLE IF NOT EXISTS ejemploTest (
                            id SERIAL PRIMARY KEY,
                            nombre VARCHAR(50) NOT NULL,
                            edad INTEGER); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabla creada correctamente")

    # Insertar datos de ejemplo
    insert_query = """ INSERT INTO ejemploTest (nombre, edad) VALUES (%s,%s)"""
    datos_ejemplo = [("Edu", 30),
                     ("María", 25),
                     ("Pedro", 35),
                     ("Ana", 28),
                     ("Luis", 40),
                     ("Laura", 22),
                     ("Carlos", 33),
                     ("Sofía", 29),
                     ("Miguel", 38)]

    cursor.executemany(insert_query, datos_ejemplo)
    connection.commit()
    print("Datos insertados correctamente")

    # Ejecutar una consulta SQL
    cursor.execute("SELECT * FROM ejemplo;")
    
    # Obtener los resultados
    records = cursor.fetchall()
    print("\nRegistros en la tabla ejemplo:")
    for record in records:
        print(record)

except (Exception, Error) as error:
    print("Error al conectar a PostgreSQL:", error)
finally:
    # Cerrar la conexión
    if connection:
        cursor.close()
        connection.close()
        print("\nConexión cerrada")
