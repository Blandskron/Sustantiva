BEGIN;
-- Realizar operaciones dentro de la transacción
INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 30);
UPDATE usuarios SET edad = 31 WHERE nombre = 'Pedro';
