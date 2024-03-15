DROP TABLE IF EXISTS finanzas_personales;

CREATE TABLE finanzas_personales
(
    nombre character varying(20) COLLATE pg_catalog."default" NOT NULL,
    me_debe integer,
    cuotas_cobrar integer,
    le_debo integer,
    cuotas_pagar integer,
    CONSTRAINT finanzas_personales_pkey PRIMARY KEY (nombre)
);

insert into finanzas_personales (nombre, me_debe, cuotas_cobrar, le_debo, cuotas_pagar)
values ('tía carmen', 0, 0, 5000, 1);
insert into finanzas_personales (nombre, me_debe, cuotas_cobrar, le_debo, cuotas_pagar)
values ('papá', 0, 0, 15000, 3);
insert into finanzas_personales (nombre, me_debe, cuotas_cobrar, le_debo, cuotas_pagar)
values ('nacho', 10000, 2, 7000, 1);
insert into finanzas_personales (nombre, me_debe, cuotas_cobrar, le_debo, cuotas_pagar)
values ('almacén esquina', 0, 0, 13000, 2);
insert into finanzas_personales (nombre, me_debe, cuotas_cobrar, le_debo, cuotas_pagar)
values ('vicios varios', 0, 0, 35000, 35);
insert into finanzas_personales (nombre, me_debe, cuotas_cobrar, le_debo, cuotas_pagar)
values ('compañero trabajo', 50000, 5, 0, 0);

select * from finanzas_personales ;