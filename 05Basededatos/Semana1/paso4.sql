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
