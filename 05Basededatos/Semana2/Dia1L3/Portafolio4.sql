CREATE TABLE Ciudades (
	ID_ciudad INT PRIMARY KEY,
	nombre VARCHAR(50)
);

CREATE TABLE Clientes (
	ID_cliente INT PRIMARY KEY,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	ID_ciudad INT,
	FOREIGN KEY (ID_ciudad) REFERENCES Ciudades(ID_ciudad)
);

ALTER TABLE Clientes
ADD email VARCHAR(50);

ALTER TABLE Clientes 
ALTER COLUMN email DROP NOT NULL;

DELETE FROM Clientes WHERE ID_cliente = 104;

ALTER TABLE Clientes 
ALTER COLUMN apellido SET NOT NULL;

ALTER TABLE Clientes 
ALTER COLUMN apellido DROP NOT NULL;

INSERT INTO Ciudade (ID_ciudad, nombre) VALUES
(1, 'Santiago'),
(2, 'Talca'),
(3, 'Curico')

INSERT INTO Clientes (ID_Cliente, nombre, apellido, ID_ciudad, email) VALUES
(104, 'Guillermo', 'Garcia', 2, NULL)

DROP TABLE IF EXISTS Empleados;

CREATE TABLE Empleados (
	ID_empleado INT PRIMARY KEY,
	nombre VARCHAR(50)
)

TRUNCATE TABLE Clientes;














--Crear una tabla llamada "Clientes" con los siguientes campos:
CREATE TABLE Clientes (
    ID_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    ID_ciudad INT,
    email VARCHAR(100)
);

--Crear un modelo de datos con integridad referencial asegurándote de que exista una tabla llamada "Ciudades" que la tabla "Clientes" pueda referenciar:
CREATE TABLE Ciudades (
    ID_ciudad INT PRIMARY KEY,
    nombre_ciudad VARCHAR(100)
);

ALTER TABLE Clientes
ADD CONSTRAINT fk_ciudad
FOREIGN KEY (ID_ciudad) REFERENCES Ciudades(ID_ciudad);

--Modificar la tabla para agregar el campo "email" a la tabla "Clientes":
ALTER TABLE Clientes
ADD email VARCHAR(100);

--Cambiar la condición de nulidad para el campo "email" para permitir valores nulos:
ALTER TABLE Clientes
ALTER COLUMN email VARCHAR(100) NULL;

--Eliminar una tabla (en este caso "Empleados") si existe, si no, créala para eliminarla:
DROP TABLE IF EXISTS Empleados;

--Truncar los datos de la tabla "Ventas" sin eliminar la estructura de la tabla:
TRUNCATE TABLE Ventas;

--Por último, crear todas las tablas necesarias según lo requerido y poblarlas con al menos 10 datos. Suponiendo que ya hemos creado la tabla "Ciudades" y "Clientes", podemos poblarlas de la siguiente manera:
-- Población de la tabla Ciudades
INSERT INTO Ciudades (ID_ciudad, nombre_ciudad) VALUES
(1, 'Ciudad A'),
(2, 'Ciudad B'),
(3, 'Ciudad C'),
(4, 'Ciudad D'),
(5, 'Ciudad E'),
(6, 'Ciudad F'),
(7, 'Ciudad G'),
(8, 'Ciudad H'),
(9, 'Ciudad I'),
(10, 'Ciudad J');

-- Población de la tabla Clientes
INSERT INTO Clientes (ID_cliente, nombre, apellido, ID_ciudad, email) VALUES
(1, 'Cliente1', 'Apellido1', 1, 'cliente1@example.com'),
(2, 'Cliente2', 'Apellido2', 2, 'cliente2@example.com'),
(3, 'Cliente3', 'Apellido3', 3, 'cliente3@example.com'),
(4, 'Cliente4', 'Apellido4', 4, 'cliente4@example.com'),
(5, 'Cliente5', 'Apellido5', 5, 'cliente5@example.com'),
(6, 'Cliente6', 'Apellido6', 6, 'cliente6@example.com'),
(7, 'Cliente7', 'Apellido7', 7, 'cliente7@example.com'),
(8, 'Cliente8', 'Apellido8', 8, 'cliente8@example.com'),
(9, 'Cliente9', 'Apellido9', 9, 'cliente9@example.com'),
(10, 'Cliente10', 'Apellido10', 10, 'cliente10@example.com');
