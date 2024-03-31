--Crear la tabla "clientes" con los campos especificados:
CREATE TABLE clientes (
    ID INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT
);

--Insertar al menos tres registros ficticios:
INSERT INTO clientes (ID, nombre, apellido, edad) VALUES
(1, 'Juan', 'Pérez', 30),
(2, 'María', 'González', 28),
(3, 'Luis', 'Martínez', 35);

--Utilizar SQL para escribir una consulta que recupere todos los clientes cuya edad sea mayor a 25 años:
SELECT * FROM clientes WHERE edad > 25;
