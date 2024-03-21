DROP TABLE IF EXISTS bandas;
CREATE TABLE bandas
(
    nombre character varying(50)
    pais character varying(50)
);

insert into bandas (nombre, pais) values ('Kraftwerk', 'Almania');
insert into bandas (nombre, pais) values ('Los prisioneros', 'Chile');
insert into bandas (nombre, pais) values ('KMFDM', 'Almania');
insert into bandas (nombre, pais) values ('Muse', 'UK');
insert into bandas (nombre, pais) values ('Th Chemical Brothers', 'UK');
insert into bandas (nombre, pais) values ('TOOL', 'USA');
insert into bandas (nombre, pais) values ('The Beatles', 'UK');
insert into bandas (nombre, pais) values ('Modeselektor', 'Almania');

DROP TABLE IF EXISTS bandas_discos;
CREATE TABLE bandas_discos
(
    nombre_disco character varying(50),
    nombre_banda character varying(50),
    anio_disco integer
)

insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Kraftwerk', 'Computer World', 1981);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Kraftwerk', 'The Man Machine', 1978);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Los Prisioneros', 'La cultura de la basura', 1987);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Los Prisioneros', 'Corazones', 1990);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('KMFDM', 'NIHIL', 1995);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('KMFDM', 'XTORT', 1996);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('KMFDM', 'ADIOS', 1999);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Muse', 'Showbiz', 1999);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Muse', 'Origin of symetry', 2001);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Muse', 'Black holes and Revelations', 2006);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Chemical Brothers', 'Surrender', 1999);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Chemical Brothers', 'Born in the echoes', 2015);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Chemical Brothers', 'No Geography', 2019);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('TOOL', 'Aenima', 1996);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('TOOL', 'Lateralus', 2001);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('TOOL', 'Fear Inoculum', 2019);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Beatles', 'Rubber Soul', 1965);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Beatles', 'Revolver', 1966);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Beatles', 'Abbey Road', 1969);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Modeslektor', 'Hello Mom!', 2005);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Modeslektor', 'Monkeytown', 2011);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Modeslektor', 'Who Else', 2019);
