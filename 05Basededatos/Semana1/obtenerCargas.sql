SELECT 
    CONCAT(Empleado.Nombre, ' ', Empleado.PrimerApellido, ' ', Empleado.SegundoApellido) AS NombreCompleto
FROM 
    Empleado
JOIN 
    CargaFam ON Empleado.Rut = CargaFam.Emprut
GROUP BY 
    Empleado.Rut
HAVING 
    COUNT(*) >= 2;
