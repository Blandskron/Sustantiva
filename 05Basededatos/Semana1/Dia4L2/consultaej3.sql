--Listar todos los discos de bandas no alemanas que hayan sido publicados desde el 2000 en adelante:
SELECT bd.nombre_banda, bd.nombre_disco, bd.anio_disco
FROM bandas_discos bd
INNER JOIN bandas b ON bd.nombre_banda = b.nombre
WHERE b.pais != 'Almania' AND bd.anio_disco >= 2000;

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
WHERE b.pais = 'Almania' AND b.nombre LIKE '%k%' AND bd.anio_disco >= 1999;

--Listar todas las bandas y el número de discos registrados:
SELECT b.nombre, COUNT(bd.nombre_disco) AS numero_discos
FROM bandas b
LEFT JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
GROUP BY b.nombre;

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
