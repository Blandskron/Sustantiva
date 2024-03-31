
-- Llenar la tabla UbicacionDpto con datos aleatorios
INSERT INTO UbicacionDpto (Numero, Ubicacion) VALUES
(1, 'Oficina 101'),
(2, 'Planta Baja'),
(3, 'Piso 3'),
(4, 'Edificio A - Piso 5'),
(5, 'Torre Norte - Piso 2');

-- Llenar la tabla Departamento con datos aleatorios
INSERT INTO Departamento (Numero, Nombre, RutGerente, GerenteInicio, Ubicacion) VALUES
(101, 'Recursos Humanos', '123456789', '2023-01-01', 1),
(102, 'Contabilidad', '987654321', '2022-12-15', 2),
(103, 'Desarrollo de Software', '456789123', '2023-05-20', 3),
(104, 'Ventas', '321654987', '2023-03-10', 4),
(105, 'Marketing', '654321987', '2022-11-28', 5);

-- Llenar la tabla Proyecto con datos aleatorios
INSERT INTO Proyecto (Numero, Nombre, Ubicacion, DptoNum) VALUES
(1, 'Proyecto Alpha', 'Oficina 101', 101),
(2, 'Proyecto Beta', 'Piso 3', 103),
(3, 'Proyecto Gamma', 'Planta Baja', 102),
(4, 'Proyecto Delta', 'Edificio A - Piso 5', 104),
(5, 'Proyecto Épsilon', 'Torre Norte - Piso 2', 105);

-- Llenar la tabla Empleado con datos aleatorios
INSERT INTO Empleado (Rut, Nombre, PrimerApellido, SegundoApellido, Fnac, Direccion, Sexo, Sueldo, RutSupervisor, NumDpto) VALUES
('1122334455', 'Juan', 'García', 'Pérez', '1990-05-15', 'Calle Principal 123', 'M', 2500.00, NULL, 101),
('2233445566', 'María', 'López', 'Martínez', '1995-08-20', 'Avenida Central 456', 'F', 2800.50, '1122334455', 101),
('3344556677', 'Carlos', 'Rodríguez', 'Gómez', '1988-03-10', 'Calle Secundaria 789', 'M', 3200.75, NULL, 103),
('4455667788', 'Ana', 'Martín', 'Sánchez', '1992-11-28', 'Avenida Principal 987', 'F', 3000.00, '3344556677', 103),
('5566778899', 'Pedro', 'Díaz', 'Fernández', '1998-07-03', 'Calle Secundaria 654', 'M', 2700.25, '3344556677', 103);

-- Llenar la tabla CargaFam con datos aleatorios
INSERT INTO CargaFam (Emprut, NombreCarga, Sexo, Fnac, Parentesco) VALUES
('1122334455', 'Laura García', 'F', '2010-02-10', 'Hija'),
('1122334455', 'Manuel García', 'M', '2015-09-18', 'Hijo'),
('2233445566', 'Lucía López', 'F', '2017-11-25', 'Hija'),
('3344556677', 'Pablo Rodríguez', 'M', '2020-06-30', 'Hijo'),
('4455667788', 'Sofía Martín', 'F', '2019-04-05', 'Hija');

-- Llenar la tabla TrabajaEn con datos aleatorios
INSERT INTO TrabajaEn (RutEmpleado, NumProyecto) VALUES
('1122334455', 1),
('2233445566', 2),
('3344556677', 2),
('4455667788', 3),
('5566778899', 3);
