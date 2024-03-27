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
	
SELECT 
	rs.nombre AS nombre_actor,
	rs.sueldo AS Sueldo_soltera
FROM 
	reparto_soltera_otra_vez rs
LEFT JOIN
	reparto_papi_ricky rp ON rs.nombre = rp.nombre
WHERE 
	rp.nombre IS NULL AND rs.sueldo > 90
ORDER BY
	nombre_actor;
	
SELECT nombre, sueldo FROM reparto_soltera_otra_vez
WHERE sueldo < 85 
EXCEPT 
SELECT nombre, sueldo FROM reparto_papi_ricky
WHERE sueldo < 85
UNION 
SELECT nombre, sueldo FROM reparto_papi_ricky
WHERE sueldo < 85
EXCEPT
SELECT nombre, sueldo FROM reparto_soltera_otra_vez
WHERE sueldo < 85 

SELECT nombre_actor, sueldo
FROM (
	SELECT nombre AS nombre_actor, sueldo
	FROM reparto_soltera_otra_vez
	WHERE sueldo < 85
	UNION
	SELECT nombre AS nombre_actor, sueldo
	FROM reparto_papi_ricky
	WHERE sueldo < 85
) AS actores_sueldo_bajo
GROUP BY nombre_actor, sueldo
HAVING COUNT(*) = 1;

SELECT COALESCE(rs.nombre, rp.nombre) AS nombre_actor,
	COALESCE(rs.sueldo, rp.sueldo) AS sueldo
FROM
	reparto_soltera_otra_vez rs
LEFT JOIN
	reparto_papi_ricky rp ON rs.nombre = rp.nombre
WHERE
	rs.sueldo < 85 AND rp.nombre IS NULL
UNION
SELECT COALESCE(rs.nombre, rp.nombre) AS nombre_actor,
	COALESCE(rs.sueldo, rp.sueldo) AS sueldo
FROM
	reparto_soltera_otra_vez rs
RIGHT JOIN
	reparto_papi_ricky rp ON rs.nombre = rp.nombre
WHERE
	rp.sueldo < 85 AND rs.nombre IS NULL
  