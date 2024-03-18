-- Actualizar la edad de un usuario específico
UPDATE usuarios SET edad = 31 WHERE nombre = 'Juan';

-- Actualizar varios usuarios a la vez
UPDATE usuarios SET edad = edad + 1 WHERE edad < 30;
