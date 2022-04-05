drop database facturation;
create database facturation;
use facturation;


CREATE TABLE clients (
    id_client BIGINT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_client VARCHAR(50) NOT NULL,
    prenom_client VARCHAR(50) NOT NULL,
    tel_client VARCHAR(20) NOT NULL
);

CREATE TABLE factures (
    id_facture BIGINT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    numero_facture INT(20) NOT NULL
);

CREATE TABLE villes (
    id_ville BIGINT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_ville VARCHAR(50) NOT NULL,
    cp_ville VARCHAR(20) NOT NULL
);

alter table clients 
add column id_ville bigint(20) not null,
add constraint foreign key (id_ville) references villes (id_ville);

alter table factures 
add column id_client bigint(20) not null,
add constraint foreign key (id_client) references clients (id_client);

insert into villes(nom_ville, cp_ville) values 
("paris", 92000),
("toulouse", 31000),
("agen", 47000);

insert into clients(nom_client, prenom_client, tel_client, id_ville) values 
("dietrich","valentin", 0634567890, 2),
("corin", "gaetan", 0684418870, 3),
("cannappin","gogulavasan",0698765432, 1);

insert into factures(numero_facture, id_client) values
("1234", 2),
("5678", 1),
("9012", 1);
