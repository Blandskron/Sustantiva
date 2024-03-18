BEGIN;
UPDATE usuarios SET edad = 32 WHERE nombre = 'Laura';
-- Ocurrió un error, revertir la transacción
ROLLBACK;
