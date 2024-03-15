-- Consulta para obtener la cantidad total de pedidos por usuario
SELECT u.Nombre, COUNT(p.ID) AS TotalPedidos
FROM Usuarios u
LEFT JOIN Pedidos p ON u.ID = p.UsuarioID
GROUP BY u.Nombre;
