--PARTE1

SELECT
	rs.nombre AS actor,
	rs.sueldo AS sueldo_soltera,
	rp.sueldo AS sueldo_papi,
	rs.sueldo + rp.sueldo AS sueldo_total
FROM
	reparto_soltera_otra_vez rs
INNER JOIN
	reparto_papi_ricky rp ON rs.nombre = rp.nombre
ORDER BY
	actor;
	

SELECT
	rs.nombre AS actor_soltera,
	rs.sueldo AS sueldo_soltera
FROM
	reparto_soltera_otra_vez rs
LEFT JOIN
	reparto_papi_ricky rp ON rs.nombre = rp.nombre
WHERE
	rp.nombre IS NULL AND rs.sueldo > 90;


SELECT
	COALESCE(rs.nombre, rp.nombre) AS nombre,
	COALESCE(rs.sueldo, rp.sueldo) AS sueldo
FROM
	reparto_soltera_otra_vez rs
FULL OUTER JOIN
	reparto_papi_ricky rp ON rs.nombre = rp.nombre
WHERE
	(rs.sueldo < 85 AND rp.nombre IS NULL) 
	OR 
	(rp.sueldo < 85 AND rs.nombre IS NULL);

--PARTE2

CREATE TABLE Actores (
	ID_actor SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	sueldo INT,
	protagonico BOOLEAN
);

CREATE TABLE Teleseries (
	ID_teleserie SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	temporada INT
);

CREATE TABLE Reparto_actores (
	ID_actor INT,
	ID_teleserie INT,
	FOREIGN KEY (ID_actor) REFERENCES Actores(ID_actor),
	FOREIGN KEY (ID_teleserie) REFERENCES Teleseries(ID_teleserie)
);
