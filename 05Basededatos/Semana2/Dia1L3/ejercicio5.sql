CREATE TABLE Usuario (
	ID_Rut VARCHAR(50) PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	telefono INT NOT NULL,
	email VARCHAR(50) NULL
);

CREATE TABLE Autor (
	ID_autor INT PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	edad INT NULL,
	nacionalidad VARCHAR(50) NULL
);

CREATE TABLE Libro (
	ID_libro INT PRIMARY KEY,
	titulo VARCHAR(50) NOT NULL,
	fecha_publicacion DATE NOT NULL,
	ediciones INT NULL,
	genero VARCHAR(50) NULL,
	ejemplar INT NOT NULL,
	ID_autor INT,
	FOREIGN KEY (ID_autor) REFERENCES Autor(ID_autor)
);

CREATE TABLE Prestamo (
	ID_prestamo INT PRIMARY KEY,
	ID_libro INT,
	ID_rut VARCHAR(50),
	fecha_prestamo DATE,
	fecha_entrega DATE,
	FOREIGN KEY (ID_libro) REFERENCES Libro(ID_libro),
	FOREIGN KEY (ID_rut) REFERENCES Usuario(ID_rut)
)

-- Tabla Autor
INSERT INTO Autor (ID_autor, nombre, apellido, edad, nacionalidad)
VALUES
    (1, 'Gabriel', 'García Márquez', 71, 'Colombiano'),
    (2, 'Isabel', 'Allende Llona', 79, 'Chilena'),
    (3, 'Mario', 'Vargas Llosa', 86, 'Peruano'),
    (4, 'Paulo', 'Coelho', 75, 'Brasileño'),
    (5, 'Patricio', 'Pimienta', 57, 'Chileno');

-- Tabla Libro
INSERT INTO Libro (ID_libro, titulo, fecha_publicacion, ediciones, genero, ejemplar, ID_autor)
VALUES
    (101, 'Cien años de soledad', '1967-01-01', 2, 'Realismo Mágico', 3, 1),
    (102, 'Crónica de una muerte anunciada', '1981-01-01', 1, 'Realismo Mágico', 5, 1),
    (103, 'La casa de los espíritus', '1982-03-23', 2, 'Realismo Mágico', 3, 2),
    (104, 'Eva Luna', '1987-01-01', 1, 'Ficción', 4, 2),
    (105, 'La ciudad y los perros', '1963-01-01', 1, 'Novela', 2, 3),
    (106, 'La tía Julia y el escribidor', '1977-01-01', 1, 'Ficción', 3, 3),
    (107, 'El alquimista', '1988-01-01', 1, 'Espiritual', 6, 4),
    (108, 'Veronika decide morir', '1998-01-01', 1, 'Ficción', 7, 4),
    (109, 'Los secretos de la pimienta', '2010-01-01', 1, 'Gastronomía', 1, 5),
    (110, 'El jardín de las especias', '2015-01-01', 1, 'Gastronomía', 2, 5);

-- Insertar 10 usuarios
INSERT INTO Usuario (ID_Rut, nombre, apellido, telefono, email)
VALUES
    ('11111111-1', 'Juan', 'Pérez', 987654321, 'juan.perez@example.com'),
    ('22222222-2', 'María', 'González', 912345678, 'maria.gonzalez@example.com'),
    ('33333333-3', 'Pedro', 'Rodríguez', 945678912, 'pedro.rodriguez@example.com'),
    ('44444444-4', 'Ana', 'López', 956789123, 'ana.lopez@example.com'),
    ('55555555-5', 'Carlos', 'Martínez', 967891234, 'carlos.martinez@example.com'),
    ('66666666-6', 'Laura', 'Sánchez', 978912345, 'laura.sanchez@example.com'),
    ('77777777-7', 'Diego', 'Fernández', 989123456, 'diego.fernandez@example.com'),
    ('88888888-8', 'Isabel', 'Torres', 990123456, 'isabel.torres@example.com'),
    ('99999999-9', 'Andrés', 'Ramírez', 901234567, 'andres.ramirez@example.com'),
    ('10101010-0', 'Valentina', 'Hernández', 912345678, 'valentina.hernandez@example.com');

INSERT INTO Prestamo (ID_prestamo,ID_libro, ID_rut, fecha_prestamo, fecha_entrega)
VALUES (1, 101, '11111111-1', '2024-03-26', '2024-04-26');

-- Actualizar la cantidad de ejemplares en la tabla Libro
UPDATE Libro
SET ejemplar = ejemplar - 1
WHERE ID_libro = 101;
