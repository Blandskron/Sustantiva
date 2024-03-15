-- Consulta para obtener los usuarios que han realizado pedidos de un producto específico
SELECT u.Nombre, p.Producto, p.Cantidad
FROM Usuarios u
JOIN Pedidos p ON u.ID = p.UsuarioID
WHERE p.Producto = 'ProductoX';
