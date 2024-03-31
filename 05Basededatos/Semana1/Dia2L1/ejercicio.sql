-- Crear la tabla de ubicaciones de departamentos
-- https://mockaroo.com/
CREATE TABLE UbicacionDpto (
    Numero INT PRIMARY KEY,
    Ubicacion VARCHAR(255)
);

-- Crear la tabla de departamentos
CREATE TABLE Departamento (
    Numero INT PRIMARY KEY,
    Nombre VARCHAR(100),
    RutGerente VARCHAR(10),
    GerenteInicio DATE, -- Cambio de GerFinic a GerenteInicio
    Ubicacion INT,
    FOREIGN KEY (Ubicacion) REFERENCES UbicacionDpto(Numero)
);

-- Crear la tabla de proyectos
CREATE TABLE Proyecto (
    Numero INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Ubicacion VARCHAR(255),
    DptoNum INT,
    FOREIGN KEY (DptoNum) REFERENCES Departamento(Numero)
);

-- Crear la tabla de empleados
CREATE TABLE Empleado (
    Rut VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(100),
    PrimerApellido VARCHAR(100),
    SegundoApellido VARCHAR(100),
    Fnac DATE,
    Direccion VARCHAR(255),
    Sexo CHAR(1),
    Sueldo DECIMAL(10,2),
    RutSupervisor VARCHAR(10),
    NumDpto INT,
    FOREIGN KEY (NumDpto) REFERENCES Departamento(Numero)
);

-- Crear la tabla de cargas familiares
CREATE TABLE CargaFam (
    Emprut VARCHAR(10),
    NombreCarga VARCHAR(100),
    Sexo CHAR(1),
    Fnac DATE,
    Parentesco VARCHAR(100),
    PRIMARY KEY (Emprut, NombreCarga),
    FOREIGN KEY (Emprut) REFERENCES Empleado(Rut)
);

-- Crear la tabla de relación entre empleados y proyectos
CREATE TABLE TrabajaEn (
    RutEmpleado VARCHAR(10),
    NumProyecto INT,
    PRIMARY KEY (RutEmpleado, NumProyecto),
    FOREIGN KEY (RutEmpleado) REFERENCES Empleado(Rut),
    FOREIGN KEY (NumProyecto) REFERENCES Proyecto(Numero)
);
