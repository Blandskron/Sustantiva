--Listar todos los discos de bandas no alemanas que hayan sido publicados desde el 2000 en adelante:
SELECT bd.nombre_banda, bd.nombre_disco, bd.anio_disco
FROM bandas_discos bd
INNER JOIN bandas b ON bd.nombre_banda = b.nombre
WHERE b.pais != 'Alemania' AND bd.anio_disco >= 1900;

UPDATE bandas SET pais = 'Alemania' WHERE pais = 'Almania'
UPDATE bandas SET nombre = 'Los Prisioneros' WHERE pais = 'Chile'
UPDATE bandas_discos SET nombre_banda = 'Modeselektor' WHERE nombre_banda = 'Modeslektor'

--Listar el disco más reciente de las bandas inglesas que terminan en 's':
SELECT nombre_banda, nombre_disco, anio_disco
FROM bandas_discos
WHERE nombre_banda IN (
    SELECT nombre
    FROM bandas
    WHERE pais = 'UK' AND nombre LIKE '%s'
)
ORDER BY anio_disco DESC
LIMIT 1;

--Listar todas las bandas alemanas con al menos una letra 'k' en su nombre que tenga discos publicados en 1999 o superior:
SELECT b.nombre, bd.nombre_disco, bd.anio_disco
FROM bandas b
INNER JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
WHERE b.pais = 'Alemania' AND b.nombre LIKE '%k%' AND bd.anio_disco >= 1999 OR b.nombre LIKE 'K%' AND bd.anio_disco >= 1999 OR b.nombre LIKE '%k' AND bd.anio_disco >= 1999;

--Listar todas las bandas y el número de discos registrados:
SELECT b.nombre, COUNT(bd.nombre_disco) AS numero_discos
FROM bandas b
LEFT JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
GROUP BY b.nombre;

SELECT nombre_banda, anio_disco FROM bandas_discos ORDER BY anio_disco ASC;

--Mostrar todos los años en que todas las bandas sacaron un disco. Ordene la lista por año:
SELECT anio_disco
FROM bandas_discos
GROUP BY anio_disco
HAVING COUNT(DISTINCT nombre_banda) = (SELECT COUNT(*) FROM bandas)
ORDER BY anio_disco;

--Listar todas las bandas que tienen un disco con nombre empezando en 'a'. Listar el nombre de la banda y del disco:
SELECT bd.nombre_banda, bd.nombre_disco
FROM bandas_discos bd
WHERE bd.nombre_disco LIKE 'A%'
GROUP BY bd.nombre_banda, bd.nombre_disco;

--Listar todas las bandas que tengan discos con más de una palabra. Listar el nombre de la banda y el disco:
SELECT bd.nombre_banda, bd.nombre_disco
FROM bandas_discos bd
WHERE bd.nombre_disco LIKE '% %';

--Listar todas las bandas que tengan discos con más de una palabra. Listar el nombre de la banda y la cantidad de discos:
SELECT b.nombre, COUNT(bd.nombre_disco) AS cantidad_discos
FROM bandas b
INNER JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
WHERE bd.nombre_disco LIKE '% %'
GROUP BY b.nombre;




PORTAFOLIO3.SQL

CREATE TABLE Empleados (
	ID_empleado INT PRIMARY KEY,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	salario INT
);

INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(1, 'Matias', 'Cataldo', 1000000),
(2, 'Rodrigo', 'Jara', 5000000),
(3, 'Rodrigo', 'Diaz', 7000000),
(4, 'Camila', 'Herrera', 8500000),
(5, 'Claudia', 'Martinez', 9000000),
(6, 'Jannet', 'Prado', 5000000)

UPDATE Empleados SET salario = 480000 WHERE ID_empleado = 5;

DELETE FROM Empleados WHERE ID_empleado = 1;

INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(7, 'Nicolas', 'Jofre', 480000),
(8, 'Florencia', 'Mellado', 180000)

CREATE SEQUENCE seq_empleados START WITH 9 INCREMENT BY 1;

INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(NEXTVAL('seq_empleados'), 'Sebastian', 'Lobos', 2500000);


INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(NEXTVAL('seq_empleados'), 'Alberto', 'Robles', 1300000),
(NEXTVAL('seq_empleados'), 'Jorge', 'Rueger', 1500000),
(NEXTVAL('seq_empleados'), 'Catalina', 'Ruiz', 1500000),
(NEXTVAL('seq_empleados'), 'Ada', 'Ramirez', 1300000);

CREATE TABLE Departamento (
	ID_departamento INT PRIMARY KEY,
	nombre VARCHAR(50),
	ID_empleado INT,
	FOREIGN KEY (ID_empleado) REFERENCES Empleados(ID_empleado)
);



