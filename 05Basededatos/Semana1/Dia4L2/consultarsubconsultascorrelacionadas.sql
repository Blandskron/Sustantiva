-- Consulta para obtener los usuarios que han realizado más pedidos que el promedio
SELECT u.Nombre
FROM Usuarios u
WHERE (SELECT COUNT(*) FROM Pedidos p WHERE p.UsuarioID = u.ID) >
      (SELECT AVG(COUNT(*)) FROM Pedidos GROUP BY UsuarioID);
