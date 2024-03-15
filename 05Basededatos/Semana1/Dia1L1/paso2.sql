CREATE TABLE Departamento (
    Numero INT PRIMARY KEY,
    Nombre VARCHAR(100),
    RutGerente VARCHAR(10),
    GerenteInicio DATE,
    Ubicacion INT,
    FOREIGN KEY (Ubicacion) REFERENCES UbicacionDpto(Numero)
);
