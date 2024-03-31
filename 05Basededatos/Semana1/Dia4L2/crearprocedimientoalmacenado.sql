-- Crear un procedimiento almacenado que inserte un nuevo usuario
CREATE PROCEDURE InsertarUsuario (IN Nombre VARCHAR(50), IN Edad INT)
BEGIN
    INSERT INTO Usuarios (Nombre, Edad) VALUES (Nombre, Edad);
END;
