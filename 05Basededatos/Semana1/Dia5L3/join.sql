-- Crear la tabla de estudiantes
CREATE TABLE Estudiantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Crear la tabla de cursos
CREATE TABLE Cursos (
    id INT PRIMARY KEY,
    nombre_curso VARCHAR(50),
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id)
);

-- Insertar datos en la tabla de estudiantes
INSERT INTO Estudiantes (id, nombre, edad, ciudad) VALUES
(1, 'Juan', 20, 'Ciudad A'),
(2, 'María', 22, 'Ciudad B'),
(3, 'Carlos', 21, 'Ciudad C'),
(4, 'Ana', 19, 'Ciudad A'),
(5, 'Pedro', 20, 'Ciudad B');

-- Insertar datos en la tabla de cursos
INSERT INTO Cursos (id, nombre_curso, id_estudiante) VALUES
(101, 'Matemáticas', 1),
(102, 'Historia', 2),
(103, 'Ciencias', 3),
(104, 'Literatura', 4),
(105, 'Arte', 5);

--INNER JOIN: Devuelve los registros que tienen coincidencias en ambas tablas.
SELECT Estudiantes.nombre, Cursos.nombre_curso
FROM Estudiantes
INNER JOIN Cursos ON Estudiantes.id = Cursos.id_estudiante;

--LEFT JOIN: Devuelve todos los registros de la tabla izquierda (Estudiantes) y los registros coincidentes de la tabla derecha (Cursos).
SELECT Estudiantes.nombre, Cursos.nombre_curso
FROM Estudiantes
LEFT JOIN Cursos ON Estudiantes.id = Cursos.id_estudiante;

--RIGHT JOIN: Devuelve todos los registros de la tabla derecha (Cursos) y los registros coincidentes de la tabla izquierda (Estudiantes).
SELECT Estudiantes.nombre, Cursos.nombre_curso
FROM Estudiantes
RIGHT JOIN Cursos ON Estudiantes.id = Cursos.id_estudiante;

--FULL OUTER JOIN: Devuelve todos los registros cuando hay una coincidencia en cualquiera de las tablas.
SELECT Estudiantes.nombre, Cursos.nombre_curso
FROM Estudiantes
FULL OUTER JOIN Cursos ON Estudiantes.id = Cursos.id_estudiante;
