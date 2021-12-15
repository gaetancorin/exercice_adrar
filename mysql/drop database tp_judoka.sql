drop database tp_judoka;
create database tp_judoka;

use tp_judoka;

CREATE TABLE judoka (
    id_judoka BIGINT(20) PRIMARY KEY NOT NULL auto_increment,
    nom_judoka VARCHAR(50) NOT NULL,
    prenom_judoka VARCHAR(50) NOT NULL,
    date_naissance_judoka DATE NOT NULL,
    sexe_judoka tinyint(1) NOT NULL,
    id_ceinture BIGINT(20) NOT NULL
);

create table ceinture (
id_ceinture bigint(20) primary key not null auto_increment,
couleur_ceinture varchar(50) not null
);

CREATE TABLE competition (
    id_competition BIGINT(20) PRIMARY KEY NOT NULL auto_increment,
    nom_competition VARCHAR(50) NOT NULL,
    date_debut_competition DATETIME DEFAULT NULL,
    date_fin_competition DATETIME DEFAULT NULL
);


CREATE TABLE inscrire (
    id_judoka BIGINT(20),
    id_competition BIGINT(20),
    PRIMARY KEY (id_judoka , id_competition),
    FOREIGN KEY (id_judoka)
        REFERENCES judoka (id_judoka),
    FOREIGN KEY (id_competition)
        REFERENCES competition (id_competition)
);

alter table judoka
add constraint foreign key (id_ceinture) references ceinture (id_ceinture);

insert into ceinture (couleur_ceinture) values
("blanche"),
("jaune"),
("rouge"),
("noire"),
("multicolor");

insert into judoka (nom_judoka, prenom_judoka, date_naissance_judoka, sexe_judoka, id_ceinture) values
("petit", "john" , "1901-01-23", 1, 3),
("michel", "jean", "1915-02-18", 2, 1),
("parii", "pierre", "1905-04-27", 1, 5),
("miam", "pizza", "1924-07-31", 1, 4),
("denez", "crotte", "1874-06-11", 1, 1);

insert into competition (nom_competition, date_debut_competition, date_fin_competition) values
("competdevieux", "2021-11-03 09:34:21","2021-11-15 09:30:00"),
("competdetresvieux", "2021-11-17 10:25:00","2021-11-30 09:29:00"),
("competdemoyenvieux", "2021-12-14 10:11:00","2021-12-24 12:30:00"),
("competdepresquevieux", "2022-01-03 10:00:00","2022-02-21 00:00:00"),
("competdejeunevieux", "2022-04-17 12:00:00","2022-04-18 17:30:00");

insert into inscrire (id_judoka, id_competition) values
("1","1"),
("2","1"),
("2","2"),
("3","2"),
("4","2");

