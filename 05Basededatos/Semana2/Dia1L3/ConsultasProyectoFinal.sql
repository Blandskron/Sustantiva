--Parte 1
--Para obtener todos los actores que participaron en ambas teleseries, junto con sus sueldos en cada una y la suma de ambos sueldos, ordenados por el nombre del actor:
SELECT 
    rs.nombre AS actor,
    rs.sueldo AS sueldo_soltera_otra_vez,
    rp.sueldo AS sueldo_papi_ricky,
    rs.sueldo + rp.sueldo AS suma_sueldos
FROM 
    reparto_soltera_otra_vez rs
INNER JOIN 
    reparto_papi_ricky rp ON rs.nombre = rp.nombre
ORDER BY 
    actor;

--Para obtener todos los actores que participaron exclusivamente en "Soltera Otra Vez" con un sueldo mayor a 90:
SELECT 
    nombre,
    sueldo
FROM 
    reparto_soltera_otra_vez
WHERE 
    nombre NOT IN (SELECT nombre FROM reparto_papi_ricky)
    AND sueldo > 90;

--Para obtener solo los actores con sueldo inferior a 85 que actuaron en cualquiera de las dos teleseries pero no en ambas:
SELECT 
    nombre,
    sueldo
FROM 
    (
        SELECT 
            nombre,
            sueldo,
            COUNT(*) AS num_series
        FROM 
            (
                SELECT 
                    nombre,
                    sueldo
                FROM 
                    reparto_soltera_otra_vez
                UNION ALL
                SELECT 
                    nombre,
                    sueldo
                FROM 
                    reparto_papi_ricky
            ) AS combined
        GROUP BY 
            nombre
    ) AS actor_info
WHERE 
    sueldo < 85 AND num_series = 1;

--Parte 2

+-------------------+          +----------------------+
|      Teleseries   |          |        Actores       |
+-------------------+          +----------------------+
| id_teleserie (PK) |          | id_actor (PK)        |
| titulo            |          | nombre               |
| año_estreno       |    +-----|- protagonico         |
+-------------------+    |     +----------------------+
                         |
                         |     +-----------------------+
                         +-----|      Reparto          |
                               +-----------------------+
                               | id_reparto (PK)       |
                               | id_teleserie (FK)     |
                               | id_actor (FK)         |
                               | protagonico (boolean) |
                               +-----------------------+

-- Creación de tablas
CREATE TABLE Teleseries (
    id_teleserie SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    año_estreno INTEGER
);

CREATE TABLE Actores (
    id_actor SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    protagonico BOOLEAN
);

CREATE TABLE Reparto (
    id_reparto SERIAL PRIMARY KEY,
    id_teleserie INTEGER REFERENCES Teleseries(id_teleserie),
    id_actor INTEGER REFERENCES Actores(id_actor),
    protagonico BOOLEAN
);

-- Inserts adaptados al nuevo diseño
-- Teleseries
INSERT INTO Teleseries (titulo, año_estreno) VALUES
('Soltera Otra Vez', 2012),
('Papi Ricky', 2019);

-- Actores
INSERT INTO Actores (nombre, protagonico) VALUES
('Paz Bascunan', true),
('Pablo Macaya', true),
('Cristian Arriagada', true),
('Josefina Montane', true),
('Loreto Aravena', true),
('Lorena Bosch', true),
('Nicolas Poblete', true),
('Hector Morales', true),
('Aranzazu Yankovic', true),
('Luis Gnecco', true),
('Catalina Guerra', true),
('Solange Lackington', true),
('Ignacio Garmendia', true),
('Julio Gonzalez', true),
('Antonella Orsini', true),
('Tamara Acosta', false),
('Silvia Santelices', false),
('Alejandro Trejo', false),
('Grimanesa Jimenez', false);

-- Reparto
-- Selecciona los actores protagonicos y los inserta como tal
INSERT INTO Reparto (id_teleserie, id_actor, protagonico) VALUES
(1, 1, true),
(1, 2, true),
(1, 3, true),
(1, 4, true),
(1, 5, true),
(1, 6, true),
(1, 7, true),
(1, 8, true),
(1, 9, true),
(1, 10, true),
(1, 11, true),
(1, 12, true),
(1, 13, true),
(1, 14, true),
(1, 15, true),
(2, 16, true),
(2, 17, true),
(2, 18, true),
(2, 19, true),
(2, 20, true);

-- Consulta solicitada (Teleseries y Actores de Reparto)
SELECT 
    t.titulo AS teleserie,
    a.nombre AS actor
FROM 
    Teleseries t
INNER JOIN 
    Reparto r ON t.id_teleserie = r.id_teleserie
INNER JOIN 
    Actores a ON r.id_actor = a.id_actor
WHERE 
    r.protagonico = true;
