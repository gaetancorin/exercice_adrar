drop database exercice_ticket;
create database exercice_ticket;
use exercice_ticket;

create table article (
id_article bigint(20) primary key auto_increment,
nom_article varchar(50) not null,
prix_article decimal(9,2) not null
);

create table vendeur (
id_vendeur bigint(20) primary key auto_increment,
nom_vendeur varchar(50) not null,
prenom_vendeur varchar(50) not null
);

create table ticket (
id_ticket bigint(20) primary key auto_increment,
date_ticket date not null
);

create table associer (
id_ticket bigint(20) not null,
id_article bigint(20) not null,
quantite_article decimal(9,2) not null,
primary key (id_article, id_ticket),
foreign key (id_article)
references article (id_article),
foreign key (id_ticket)
references ticket (id_ticket)
);

alter table ticket
add column id_vendeur bigint(20) not null,
add constraint foreign key (id_vendeur) references vendeur (id_vendeur);

insert into vendeur (nom_vendeur, prenom_vendeur) values
("corin","gaetan"),
("dietriche","valentin"),
("cannappin","gogulavasan"),
("richard","pierre"),
("valero","johan");

insert into ticket (date_ticket, id_vendeur) values
("2021-8-04", 1),
("2021-7-27",4),
("2021-11-05",5),
("1775-05-17",3),
("2458-02-05",3);

insert into article (nom_article, prix_article) values
("caviar",1),
("homard",1),
("truffe",1),
("safran_kg",5),
("bigmac",1);

insert into associer (id_ticket, id_article, quantite_article) values
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,4000);

