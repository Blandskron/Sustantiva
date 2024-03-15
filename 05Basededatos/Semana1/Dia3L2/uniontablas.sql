-- Crear una nueva tabla 'Pedidos' y unir con la tabla 'Usuarios'
CREATE TABLE Pedidos (
    ID INT PRIMARY KEY,
    UsuarioID INT,
    Producto VARCHAR(50),
    Cantidad INT
);

-- Consulta para obtener información del usuario y su pedido
SELECT u.Nombre, p.Producto, p.Cantidad
FROM Usuarios u
JOIN Pedidos p ON u.ID = p.UsuarioID;
