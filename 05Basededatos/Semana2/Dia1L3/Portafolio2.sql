--Crear la tabla "Productos" con los campos especificados:
CREATE TABLE Productos (
    ID_producto INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10, 2),
    categoria VARCHAR(50)
);

--ecuperar todos los productos de la tabla "Productos":
SELECT * FROM Productos;

--Seleccionar los productos cuyo precio sea superior a 50000:
SELECT * FROM Productos WHERE precio > 50000;

--Obtener la información de un producto específico utilizando su ID_producto. Por ejemplo, si el ID_producto es 1:
SELECT * FROM Productos WHERE ID_producto = 1;

--Experimentar con funciones como COUNT, AVG y MAX:
--COUNT: Obtener el número total de productos en la tabla.
SELECT COUNT(*) AS total_productos FROM Productos;

--AVG: Calcular el precio promedio de los productos.
SELECT AVG(precio) AS precio_promedio FROM Productos;

--MAX: Encontrar el precio máximo de los productos.
SELECT MAX(precio) AS precio_maximo FROM Productos;

--Poblar la tabla con 10 datos ficticios:
INSERT INTO Productos (ID_producto, nombre, precio, categoria) VALUES
(1, 'Producto A', 75000.00, 'Electrónicos'),
(2, 'Producto B', 60000.00, 'Ropa'),
(3, 'Producto C', 45000.00, 'Hogar'),
(4, 'Producto D', 55000.00, 'Electrodomésticos'),
(5, 'Producto E', 85000.00, 'Electrónicos'),
(6, 'Producto F', 30000.00, 'Hogar'),
(7, 'Producto G', 70000.00, 'Ropa'),
(8, 'Producto H', 95000.00, 'Electrodomésticos'),
(9, 'Producto I', 40000.00, 'Hogar'),
(10, 'Producto J', 5000.00, 'Electrónicos');
