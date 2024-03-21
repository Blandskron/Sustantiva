--Crear la tabla "Empleados" con los campos especificados:
CREATE TABLE Empleados (
    ID_empleado INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    salario DECIMAL(10, 2)
);

--Actualizar la información de un empleado suponiendo que el ID_empleado sea 1 para cambiar el salario:
UPDATE Empleados SET salario = nuevo_salario WHERE ID_empleado = 1;

--Borrar la información de un empleado específico suponiendo que el ID_empleado sea 2:
DELETE FROM Empleados WHERE ID_empleado = 2;

--Insertar nueva información de un empleado:
INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(nuevo_id, 'NuevoNombre', 'NuevoApellido', nuevo_salario);

--Utilizar una secuencia para asignar identificadores suponiendo que hay una secuencia llamada "seq_empleados":
CREATE SEQUENCE seq_empleados START WITH 1 INCREMENT BY 1;

--Luego, al insertar datos, no necesitas proporcionar un valor para ID_empleado, se generará automáticamente usando la secuencia.
--Insertar datos manteniendo la integridad referencial suponiendo que hay una tabla relacionada llamada "Departamento":
INSERT INTO Empleados (ID_empleado, nombre, apellido, salario, ID_departamento) 
VALUES (1, 'Nombre', 'Apellido', 50000.00, 1);

--Aquí, ID_departamento es una clave externa que hace referencia a la tabla "Departamento".
--Asegurarse de que existan restricciones en la tabla "Empleados", por ejemplo, una restricción de clave primaria en ID_empleado y una restricción de clave externa en ID_departamento:
CREATE TABLE Empleados (
    ID_empleado INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    salario DECIMAL(10, 2),
    ID_departamento INT,
    FOREIGN KEY (ID_departamento) REFERENCES Departamento(ID_departamento)
);

--Ahora, respecto a la tabla "Departamento" y su población inicial, aquí tienes un ejemplo de cómo crearla y poblarla:
CREATE TABLE Departamento (
    ID_departamento INT PRIMARY KEY,
    nombre_departamento VARCHAR(100)
);

INSERT INTO Departamento (ID_departamento, nombre_departamento) VALUES
(1, 'Ventas'),
(2, 'Recursos Humanos'),
(3, 'Finanzas'),
(4, 'Desarrollo'),
(5, 'Marketing'),
(6, 'Producción'),
(7, 'Logística'),
(8, 'Soporte Técnico'),
(9, 'Administración'),
(10, 'Calidad');