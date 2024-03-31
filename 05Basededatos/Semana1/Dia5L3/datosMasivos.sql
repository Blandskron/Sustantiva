-- Conexión a la base de datos
\c nombre_basedatos;

-- Copiar datos desde un archivo CSV a la tabla usuarios
COPY usuarios (nombre, edad) FROM 'ruta_del_archivo/usuarios.csv' DELIMITER ',' CSV HEADER;
