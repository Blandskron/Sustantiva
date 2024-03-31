CREATE TABLE CargaFam (
    Emprut VARCHAR(10),
    NombreCarga VARCHAR(100),
    Sexo CHAR(1),
    Fnac DATE,
    Parentesco VARCHAR(100),
    PRIMARY KEY (Emprut, NombreCarga),
    FOREIGN KEY (Emprut) REFERENCES Empleado(Rut)
);
