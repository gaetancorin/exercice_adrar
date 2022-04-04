create database tpLOGREGSHOW;

use tpLOGREGSHOW;

CREATE TABLE roles(
   id_role INT auto_increment,
   name_role VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_role)
)ENGINE = INNODB, CHARSET = 'utf8mb4';

CREATE TABLE users(
   id_user INT auto_increment,
   name VARCHAR(50) NOT NULL,
   first_name VARCHAR(50) NOT NULL,
   mail VARCHAR(100) NOT NULL,
   password VARCHAR(255) NOT NULL,
   image VARCHAR(255),
   id_role INT,
   PRIMARY KEY(id_user),
   FOREIGN KEY(id_role) REFERENCES roles(id_role)
)ENGINE = INNODB, CHARSET = 'utf8mb4';

INSERT INTO `roles` (`id_role`, `name_role`) 
VALUES (NULL, 'administrateur'), (NULL, 'modÃ©rateur'), (NULL, 'membre');