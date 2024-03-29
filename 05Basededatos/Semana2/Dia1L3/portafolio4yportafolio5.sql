--portafolio4.sql
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

INSERT INTO Ciudades (ID_ciudad, nombre) VALUES
(101, 'Santiago'),
(102, 'Punta arenas'),
(103, 'Viña del mar'),
(104, 'Talca'),
(105, 'Chillan');


INSERT INTO Clientes (ID_cliente, nombre, apellido, ID_ciudad, email) VALUES
(1, 'Alberto', 'Robles', 101, 'alberto@gmail.com')

INSERT INTO Clientes (ID_cliente, nombre, apellido, ID_ciudad, email) VALUES
(2, 'Eduardo', 'Castillo', 102, NULL)

DELETE FROM Clientes WHERE ID_cliente IN (1, 2);

ALTER TABLE Clientes
ALTER COLUMN email SET NOT NULL;

ALTER TABLE Clientes
ALTER COLUMN email DROP NOT NULL;

DROP TABLE IF EXISTS Empleados;

TRUNCATE TABLE Clientes;


INSERT INTO Clientes (ID_cliente, nombre, apellido, ID_ciudad, email) VALUES
(1, 'Alberto', 'Robles', 101, 'alberto@gmail.com'),
(2, 'Eduardo', 'Castillo', 102, NULL),
(3, 'Jeff', 'Palacios', 103, NULL),
(4, 'Luis', 'Vasquez', 104, 'Luis@gmail.com'),
(5, 'Matias', 'Cataldo', 101, 'Mati@gmail.com'),
(6, 'Rodrigo', 'Diaz', 101, NULL),
(7, 'Rodrigo', 'Jara', 105, NULL),
(8, 'Nicolas', 'Jofre', 102, 'Nico@gmail.com'),
(9, 'Eliot', 'Sepulveda', 103, NULL),
(10, 'Fernando', 'Clavero', 102, 'Fer@gmail.com'),
(11, 'Juan', 'Rojas', 104, NULL),
(12, 'Felipe', 'Urdanivia', 102, 'Felipe@gmail.com'),
(13, 'Ada', 'Ramirez', 105, NULL),
(14, 'Jannete', 'Prado', 102, 'prado@gmail.com'),
(15, 'Jorge', 'Rueger', 104, NULL),
(16, 'Sebastian', 'Lobos', 102, NULL)





--portafolio5.sql
CREATE TABLE Autor (
	ID_autor SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50),
	nacionalidad VARCHAR(50)
);

CREATE TABLE Lector (
	ID_lector INT PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	rut VARCHAR(50) NOT NULL,
	telefono INT,
	direccion VARCHAR(50)
);

CREATE TABLE Libro (
	ID_libro INT PRIMARY KEY,
	nombre VARCHAR(50),
	edicion VARCHAR(50),
	stock INT,
	ID_autor INT,
	FOREIGN KEY (ID_autor) REFERENCES Autor(ID_autor)
);

CREATE TABLE Prestamo (
	ID_libro INT,
	f_prestamo DATE,
	f_devolucion DATE,
	ID_lector INT,
	FOREIGN KEY (ID_libro) REFERENCES Libro(ID_libro),
	FOREIGN KEY (ID_lector) REFERENCES Lector(ID_lector)
);

INSERT INTO Autor (nombre, apellido, nacionalidad) VALUES
    ('Gabriel', 'García Márquez', 'Colombiano'),
    ('Jane', 'Austen', 'Británica'),
    ('Haruki', 'Murakami', 'Japonés'),
    ('Isabel', 'Allende', 'Chilena'),
    ('Ernest', 'Hemingway', 'Estadounidense');
	
INSERT INTO Lector (ID_lector, nombre, apellido, rut, telefono, direccion) VALUES
    (1000, 'María', 'Pérez', '12345678-9', 987654321, 'Av. Libertad 123'),
    (1001, 'Juan', 'Rodríguez', '98765432-1', 912345678, 'Calle Principal 456'),
    (1002, 'Ana', 'González', '56789123-4', 998877665, 'Plaza Central 789'),
    (1003, 'Pedro', 'López', '34567890-1', 955443322, 'Paseo del Sol 101'),
    (1004, 'Laura', 'Martínez', '23456789-0', 944332211, 'Río Azul 555');

INSERT INTO Libro (ID_libro, nombre, edicion, stock, ID_autor) VALUES
    (101, 'Cien años de soledad', 'Primera edición', 50, 1),
    (102, 'Orgullo y prejuicio', 'Edición anotada', 30, 2),
    (103, 'Tokio Blues', 'Edición especial', 20, 3),
    (104, 'La casa de los espíritus', 'Edición de lujo', 40, 4),
    (105, 'El viejo y el mar', 'Edición clásica', 15, 5);

INSERT INTO Prestamo (ID_libro, f_prestamo, f_devolucion, ID_lector) VALUES
(104, '2024-03-28', '2024-04-28', 1002);
UPDATE Libro SET stock = stock - 1 WHERE ID_libro = 104;

ALTER TABLE Prestamo
ADD COLUMN ID_prestamo SERIAL PRIMARY KEY;

UPDATE Libro
SET stock = stock + 1
WHERE ID_libro = (
    SELECT ID_libro
    FROM Prestamo
    WHERE ID_prestamo = 3
);
DELETE FROM Prestamo WHERE ID_prestamo = 3;
