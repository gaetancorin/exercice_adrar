drop database loc_voiture;
create database loc_voiture;
use loc_voiture;

CREATE TABLE responsable_agence (
    id_responsable_agence bigint(20) PRIMARY KEY AUTO_INCREMENT,
    nom_responsable VARCHAR(50) NOT NULL,
    prenom_responsable VARCHAR(50) NOT NULL,
    tel_responsable VARCHAR(50) DEFAULT NULL,
    mail_responsable varchar(100) not null
);

CREATE TABLE locaux (
    id_locaux bigINT(20) PRIMARY KEY AUTO_INCREMENT,
    adresse_locaux VARCHAR(100) NOT NULL,
    ville_locaux VARCHAR(50) NOT NULL,
    cp_locaux VARCHAR(20) not NULL
);

CREATE TABLE flotte_voitures (
    id_flotte_voitures bigINT(20) PRIMARY KEY AUTO_INCREMENT,
    loues_ou_pas_voiture tinyint(1) NOT NULL,
    marque_voiture VARCHAR(50) NOT NULL,
    couleur_voiture VARCHAR(20) not NULL
);

alter table locaux
add column id_responsable_agence bigint(20) not null,
add constraint foreign key (id_responsable_agence) references responsable_agence (id_responsable_agence);

CREATE TABLE appartenir (
    id_locaux BIGINT(20),
    id_flotte_voitures BIGINT(20),
    PRIMARY KEY (id_locaux , id_flotte_voitures),
    FOREIGN KEY (id_locaux)
        REFERENCES flotte_voitures (id_flotte_voitures),
    FOREIGN KEY (id_flotte_voitures)
        REFERENCES locaux (id_locaux)
);

insert into responsable_agence (nom_responsable, prenom_responsable, tel_responsable, mail_responsable) values
("dietrich", "valentin", 0634567890,"dietrichval@gmail.com"),
("corin", "gaetan", 0684418870, "coringaet@hotmail.fr"),
("cannappin","gogulavasan",0698765432,"cannagogu@hotmail.fr"),
("lafesse", "jean", 0611111111,"lafessejean@gmail.com");
  
insert into locaux (adresse_locaux, ville_locaux, cp_locaux, id_responsable_agence) values
("23 rue des noix", "toulouse", "31200", 1),
("11 rue de l ennuie", "adrar", "31520", 1),
("1 avenue de chez moi", "croix daurade", "31200", 3),
("4 avenue de la nouille", "paris", "92000", 2);

insert into flotte_voitures (loues_ou_pas_voiture, marque_voiture, couleur_voiture) values
(0, "mini", "bleu"),
(1, "renault", "blanc"),
(0, "peugeot", "rouge"),
(1, "opel", "marron_caca");

# EXERCICE NUMERO 2 

insert into responsable_agence (nom_responsable, prenom_responsable, tel_responsable, mail_responsable) values
("fourwheels", "joulou", 0634567890, "toukilou@atoutroule.fr");
insert into locaux (adresse_locaux, ville_locaux, cp_locaux, id_responsable_agence) values
("avenue bloblocar", "toukilou", "22222", 5);
insert into flotte_voitures (loues_ou_pas_voiture, marque_voiture, couleur_voiture) values
(0, "fiot 7014", "jaune"),
(0, "farp kagi", "orange");

update flotte_voitures
set couleur_voiture = "marron clair"
where id_flotte_voitures = 3;

alter table flotte_voitures
change marque_voiture marque_et_modele_voiture varchar(50) not null;

alter table responsable_agence
modify mail_responsable varchar(200) not null;

alter table flotte_voitures
drop column loues_ou_pas_voiture;

delete from flotte_voitures 
where id_flotte_voitures = 2;

# EXERCICE POUR LES PLUS RAPIDE

update responsable_agence
set tel_responsable = "46.25.63.14.98"
where prenom_responsable = "joulou" and nom_responsable = "fourwheels";


