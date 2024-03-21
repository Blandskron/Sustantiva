"""
Entidades Clave:

Libro
Autor
Ejemplar
Prestamo
Modelo Entidad-Relación:

lua
Copy code
+----------+       +------------+       +------------+       +-----------+
|  Libro   | ----- |  Ejemplar  | ----- |  Prestamo  |       |   Autor   |
+----------+       +------------+       +------------+       +-----------+
| id_libro |       | id_ejemplar|       | id_prestamo|       | id_autor  |
| titulo   |       | id_libro   |       | id_ejemplar|       | nombre    |
| autor    |       | estado     |       | fecha_ini  |       | apellido  |
| etc.     |       +------------+       | fecha_fin  |       | etc.      |
+----------+                            +------------+       +-----------+
Relaciones y Atributos Clave:

La relación entre Libro y Autor es (muchos a muchos), ya que un libro puede tener varios autores y un autor puede escribir varios libros. Se necesita una tabla intermedia para manejar esta relación.
La entidad Libro tiene un atributo clave (id_libro).
La entidad Autor tiene un atributo clave (id_autor).
La entidad Ejemplar tiene un atributo clave (id_ejemplar).
Entidades Principales y Relaciones:

Entidades Principales: Libro, Autor, Ejemplar, Prestamo.
Relaciones:
Libro - Autor (muchos a muchos)
Libro - Ejemplar (uno a muchos)
Ejemplar - Prestamo (uno a muchos)
Tipo de Relación:

Libro y Autor tienen una relación (muchos a muchos), manejada a través de una tabla intermedia.
Libro y Ejemplar tienen una relación (uno a muchos), ya que un libro puede tener varios ejemplares.
Ejemplar y Prestamo tienen una relación (uno a muchos), ya que un ejemplar puede ser prestado varias veces.
Entidad Débil:

La entidad Ejemplar es una entidad débil que depende de la existencia de un Libro. Esto significa que un Ejemplar no puede existir sin un Libro asociado.
Modelo Relacional:

diff
Copy code
Libro:
- id_libro (PK)
- titulo
- etc.

Autor:
- id_autor (PK)
- nombre
- apellido
- etc.

Ejemplar:
- id_ejemplar (PK)
- id_libro (FK)
- estado
- etc.

Prestamo:
- id_prestamo (PK)
- id_ejemplar (FK)
- fecha_ini
- fecha_fin
- etc.

Libro_Autor:
- id_libro (FK)
- id_autor (FK)
Reglas de Transformación:

Las entidades se convierten en tablas.
Los atributos se convierten en columnas.
Las claves primarias se mantienen como claves primarias en las tablas correspondientes.
Las relaciones se convierten en claves foráneas en las tablas relacionadas.
Tipos de Datos y Restricciones:

Se utilizan tipos de datos apropiados para cada columna (por ejemplo, VARCHAR para nombres, DATE para fechas).
Se aplican restricciones de clave primaria y foránea para garantizar la integridad de los datos.
Normalización y Desnormalización:

Se aplicará la normalización para reducir redundancias, como dividir la información de autor en una tabla separada.
La desnormalización podría ser útil en situaciones donde la optimización del rendimiento es prioritaria y las redundancias controladas no comprometen la integridad de los datos.
Diccionario de Datos:
Libro:
id_libro (PK, INT)
titulo (VARCHAR)
etc.
Autor:
id_autor (PK, INT)
nombre (VARCHAR)
apellido (VARCHAR)
etc.
Ejemplar:
id_ejemplar (PK, INT)
id_libro (FK, INT)
estado (VARCHAR)
etc.
Prestamo:
id_prestamo (PK, INT)
id_ejemplar (FK, INT)
fecha_ini (DATE)
fecha_fin (DATE)
etc.
"""

-- Tabla Libro
CREATE TABLE Libro (
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(255),
    -- Otros atributos del libro
);

-- Tabla Autor
CREATE TABLE Autor (
    id_autor INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    -- Otros atributos del autor
);

-- Tabla Ejemplar
CREATE TABLE Ejemplar (
    id_ejemplar INT PRIMARY KEY,
    id_libro INT,
    estado VARCHAR(50),
    -- Otros atributos del ejemplar
    FOREIGN KEY (id_libro) REFERENCES Libro(id_libro)
);

-- Tabla Prestamo
CREATE TABLE Prestamo (
    id_prestamo INT PRIMARY KEY,
    id_ejemplar INT,
    fecha_ini DATE,
    fecha_fin DATE,
    -- Otros atributos del préstamo
    FOREIGN KEY (id_ejemplar) REFERENCES Ejemplar(id_ejemplar)
);

-- Tabla Libro_Autor (para la relación muchos a muchos entre Libro y Autor)
CREATE TABLE Libro_Autor (
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES Libro(id_libro),
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
);

-- Datos de ejemplo para la tabla Libro
INSERT INTO Libro (id_libro, titulo) VALUES
(1, 'Libro 1'),
(2, 'Libro 2'),
(3, 'Libro 3');

-- Datos de ejemplo para la tabla Autor
INSERT INTO Autor (id_autor, nombre, apellido) VALUES
(1, 'Autor 1', 'Apellido 1'),
(2, 'Autor 2', 'Apellido 2'),
(3, 'Autor 3', 'Apellido 3');

-- Datos de ejemplo para la tabla Ejemplar
INSERT INTO Ejemplar (id_ejemplar, id_libro, estado) VALUES
(1, 1, 'Disponible'),
(2, 1, 'Prestado'),
(3, 2, 'Disponible'),
(4, 3, 'Prestado');

-- Datos de ejemplo para la tabla Prestamo
INSERT INTO Prestamo (id_prestamo, id_ejemplar, fecha_ini, fecha_fin) VALUES
(1, 2, '2024-03-15', '2024-04-15'),
(2, 4, '2024-03-10', '2024-04-10');

-- Datos de ejemplo para la tabla Libro_Autor
INSERT INTO Libro_Autor (id_libro, id_autor) VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 3);
