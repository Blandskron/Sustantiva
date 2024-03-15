SELECT 
    CONCAT(Empleado.Nombre, ' ', Empleado.PrimerApellido, ' ', Empleado.SegundoApellido) AS NombreCompleto,
    Empleado.Direccion
FROM 
    Empleado
JOIN 
    Departamento ON Empleado.NumDpto = Departamento.Numero
WHERE 
    Departamento.Nombre = 'Investigacion';
