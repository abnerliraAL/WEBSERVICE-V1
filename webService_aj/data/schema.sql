CREATE DATABASE webservice_aj;

USE webservice_aj;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table clientes(
    id_cliente integer not null PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(30) not null,
    apellido_pa varchar(30) not null,
    apellido_ma varchar(30) not null,
    telefono    varchar(30) not null,
    email       varchar(50) not null,
    utl          varchar(200) not null,
);


create table paradas(
  varchar(150) not null,

)

create table rutas(
    id_ruta varchar(5)  primary key , 
    nombre varchar(30) not null,
    punto_inicio varchar(30) not null,
    punto_final varchar(30) not null,
    hora_inicio_labor varchar(20) not null,
    hora_final_labor varchar(20) not null,
    transcurso varchar(30) not null,
    costo  varchar(10) not null,
    url_ruta varchar(200) not null);

create table cabeza(
    palabra_uno varchar(50) primary key,
    palabra_dos varchar(50) not null,
    palabra_tres varchar(50) not null, 
    palabra_cuatro varchar(50)not null,
    p1_otomi varchar(50) not null,
    p2_otomi varchar(50) not null,
    p3_otomi varchar(50) not null,
    p4_otomi varchar(50) not null);



INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'axbrenj'@'localhost' IDENTIFIED BY 'kuorra.2018'; 
GRANT ALL PRIVILEGES ON webservice_aj.* TO 'axbrenj'@'localhost'; 
FLUSH PRIVILEGES;
