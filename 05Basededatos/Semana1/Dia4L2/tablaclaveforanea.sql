-- Crear una tabla 'Pedidos' con una clave foránea que hace referencia a la tabla 'Usuarios'
CREATE TABLE Pedidos (
    ID INT PRIMARY KEY,
    UsuarioID INT,
    Producto VARCHAR(50),
    Cantidad INT,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(ID)
);
