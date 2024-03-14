CREATE TABLE Proyecto (
    Numero INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Ubicacion VARCHAR(255),
    DptoNum INT,
    FOREIGN KEY (DptoNum) REFERENCES Departamento(Numero)
);
