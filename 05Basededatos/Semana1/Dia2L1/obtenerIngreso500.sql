SELECT 
    Departamento.Nombre AS NombreDepartamento,
    COUNT(*) AS NumEmpleadosMas500k
FROM 
    Departamento
JOIN 
    Empleado ON Departamento.Numero = Empleado.NumDpto
WHERE 
    Empleado.Sueldo > 500000
GROUP BY 
    Departamento.Nombre;
