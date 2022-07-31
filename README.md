

CREATE DATABASE contactosdb;
USE contactosdb;

CREATE TABLE contactos(
    id int primary key auto_increment,
    nombres varchar(20),
    telefono varchar(20),
    email varchar(150)

);    

CREATE DATABASE spaceshipsdb;
USE spaceshipsdb;


CREATE TABLE lanzadera(
    id int PRIMARY KEY auto_increment,
    nombre VARCHAR(50),
    situacion VARCHAR(50),
    peso int,
    empuje int,
    combustible VARCHAR(50),
    objetivo VARCHAR(150),
    pais VARCHAR(50),
    fases int,

);

CREATE TABLE tripulada(
    id int PRIMARY KEY auto_increment,
    nombre VARCHAR(50),
    situacion VARCHAR(50),
    peso int,
    empuje int,
    combustible VARCHAR(50),
    objetivo VARCHAR(150),
    pais VARCHAR(50),
    capacidad int
);


CREATE TABLE naves(
    id int PRIMARY KEY auto_increment,
    nombre VARCHAR(50),
    situacion VARCHAR(50),
    peso int,
    empuje int,
    combustible VARCHAR(50),
    tipo VARCHAR(50)
);




INSERT INTO lanzadera(nombre, situacion, peso, empuje, combustible, tipo) VALUES ('Saturno V','Retirado','2900','3500''Hidrogeno Liquido', "Lanzadera");


CREATE TABLE productos(
    id int primary key auto_increment,
    producto varchar(50),
    description varchar(50),
    marca varchar(30),
    precio int,
    stock int

);

INSERT INTO productos(description,marca,precio,stock) VALUES ('Licuadora estandar', 'Oster', 25, 2);


# Eliminar una columna
ALTER TABLE productos DROP producto;

# Agregar columna
ALTER TABLE productos ADD producto VARCHAR(20) FIRST;
ALTER TABLE productos ADD producto VARCHAR(20) AFTER id;