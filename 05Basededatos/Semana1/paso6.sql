CREATE TABLE TrabajaEn (
    RutEmpleado VARCHAR(10),
    NumProyecto INT,
    PRIMARY KEY (RutEmpleado, NumProyecto),
    FOREIGN KEY (RutEmpleado) REFERENCES Empleado(Rut),
    FOREIGN KEY (NumProyecto) REFERENCES Proyecto(Numero)
);
