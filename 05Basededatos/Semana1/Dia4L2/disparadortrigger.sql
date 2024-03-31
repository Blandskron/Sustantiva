-- Crear un disparador que actualice la fecha de modificación cuando se actualice un usuario
CREATE TRIGGER ActualizarFechaModificacion
BEFORE UPDATE ON Usuarios
FOR EACH ROW
BEGIN
    SET NEW.FechaModificacion = NOW();
END;
