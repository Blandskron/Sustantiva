-- Consulta para obtener los usuarios que han realizado un pedido
SELECT * FROM Usuarios WHERE ID IN (SELECT DISTINCT UsuarioID FROM Pedidos);
