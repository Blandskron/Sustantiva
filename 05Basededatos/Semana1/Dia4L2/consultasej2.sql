--Insertar 9 series adicionales:
INSERT INTO serie_netflix (nombre, temporadas, genero, anio_estreno) VALUES
('Stranger Things', 4, 'Drama de ciencia ficción', 2016),
('The Crown', 4, 'Drama histórico', 2016),
('Breaking Bad', 5, 'Drama criminal', 2008),
('Friends', 10, 'Comedia', 1994),
('Game of Thrones', 8, 'Fantasía épica', 2011),
('The Office', 9, 'Comedia mockumental', 2005),
('Narcos', 3, 'Drama criminal', 2015),
('Money Heist', 5, 'Drama de atracos', 2017),
('Sherlock', 4, 'Drama policial', 2010);

--Listar todas las series que tengan más de 3 temporadas ordenadas por año de estreno descendente:
SELECT nombre, temporadas, anio_estreno
FROM serie_netflix
WHERE temporadas > 3
ORDER BY anio_estreno DESC;

--Listar el año de la serie más antigua:
SELECT MIN(anio_estreno) AS año_mas_antiguo
FROM serie_netflix;

--Listar el año de la serie más nueva:
SELECT MAX(anio_estreno) AS año_mas_nuevo
FROM serie_netflix;

--Mostrar el promedio del año de estreno de las series:
SELECT AVG(anio_estreno) AS promedio_anio_estreno
FROM serie_netflix;

--Listar las series que tengan 1, 2, 3, 4, 5 o 7 temporadas:
SELECT nombre, temporadas
FROM serie_netflix
WHERE temporadas IN (1, 2, 3, 4, 5, 7);

--Listar las series que no tengan 1, 2, 4, 5 o 7 temporadas:
SELECT nombre, temporadas
FROM serie_netflix
WHERE temporadas NOT IN (1, 2, 4, 5, 7);

--Borrar todas las series con año de estreno superior a 2010:
DELETE FROM serie_netflix
WHERE anio_estreno > 2010;

--Reinsertar datos borrados:
INSERT INTO serie_netflix (nombre, temporadas, genero, anio_estreno) VALUES
('Black Mirror', 5, 'Ciencia ficción', 2011);

--Agregar la serie Doctor House:
INSERT INTO serie_netflix (nombre, temporadas, genero, anio_estreno) VALUES
('Doctor House', 8, 'Drama médico', 2004);


--Listar todas las series estrenadas entre 2005 y 2020:
SELECT nombre, anio_estreno
FROM serie_netflix
WHERE anio_estreno BETWEEN 2005 AND 2020;

--Listar todas aquellas series con nombre comenzando en 'B' o terminando en 'e':
SELECT nombre
FROM serie_netflix
WHERE nombre LIKE 'B%' OR nombre LIKE '%e';

--Listar aquellas series cuyo año de estreno más la cantidad de temporadas excede 2010:
SELECT nombre, anio_estreno, temporadas
FROM serie_netflix
WHERE anio_estreno + temporadas > 2010;
