SELECT NumeroProyecto
FROM
(
    -- Proyectos donde el empleado "Perez" trabaja
    SELECT 
        NumProyecto AS NumeroProyecto
    FROM 
        TrabajaEn
    JOIN 
        Empleado ON TrabajaEn.RutEmpleado = Empleado.Rut
    WHERE 
        Empleado.PrimerApellido = 'Perez'

    UNION

    -- Proyectos donde el gerente del departamento tiene el apellido "Perez"
    SELECT 
        Proyecto.Numero AS NumeroProyecto
    FROM 
        Departamento
    JOIN 
        Empleado ON Departamento.RutGerente = Empleado.Rut
    JOIN 
        Proyecto ON Departamento.Numero = Proyecto.DptoNum
    WHERE 
        Empleado.PrimerApellido = 'Perez'
) AS ProyectosPerez;
