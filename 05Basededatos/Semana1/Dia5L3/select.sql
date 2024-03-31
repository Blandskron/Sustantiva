-- Seleccionar todos los usuarios de la tabla usuarios
SELECT * FROM usuarios;

-- Seleccionar usuarios con una edad específica
SELECT * FROM usuarios WHERE edad = 30;

-- Seleccionar usuarios cuyo nombre comience con 'J'
SELECT * FROM usuarios WHERE nombre LIKE 'J%';

-- Seleccionar usuarios ordenados por edad de forma descendente
SELECT * FROM usuarios ORDER BY edad DESC;

-- Seleccionar usuarios con límite y desplazamiento
SELECT * FROM usuarios ORDER BY id LIMIT 10 OFFSET 20;
