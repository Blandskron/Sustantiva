-- A quién le debe más dinero:
SELECT nombre
FROM finanzas_personales
WHERE le_debo = (SELECT MAX(le_debo) FROM finanzas_personales);

--Quién le debe más dinero:
SELECT nombre
FROM finanzas_personales
WHERE me_debe = (SELECT MAX(me_debe) FROM finanzas_personales);

--Cuánto dinero debe en total:
SELECT SUM(le_debo) AS total_debe
FROM finanzas_personales;

--Cuánto dinero debe en promedio:
SELECT AVG(le_debo) AS promedio_debe
FROM finanzas_personales;

--Suponiendo que no puede pagar más de una deuda al mes, ¿cuántos meses tarda en pagar la cuenta?:
SELECT nombre,
       CEIL(le_debo / cuotas_pagar) AS meses_para_pagar
FROM finanzas_personales;

--Suponiendo que le pagan todo lo que le deben el mismo día y usa eso para pagar sus deudas, ¿qué valor actual tendría la deuda?:
SELECT nombre,
       (le_debo - (cuotas_pagar * cuotas_cobrar)) AS deuda_actual
FROM finanzas_personales;
