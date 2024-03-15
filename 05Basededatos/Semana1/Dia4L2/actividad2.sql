DROP TABLE IF EXISTS serie_netflix;
CREATE TABLE serie_netflix
(
    nombre character varying NOT NULL,
    temporadas integer,
    genero character varying(50),
    anio_estreno integer,
    PRIMARY KEY (nombre)
);

insert into serie_netflix (nombre, temporadas, genero, anio_estreno) values ('Black Mirror', 5, 'Ciencia ficción', 2011);

select * from serie_netflix;