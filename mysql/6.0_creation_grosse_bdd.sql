drop database usine_production;
create database usine_production;
use usine_production;

create table droit (
id_droit bigint(20) primary key not null auto_increment,
droit varchar(50) not null
);

create table utilisateur (
id_utilisateur bigint(20) primary key not null auto_increment,
identifiant_utilisateur varchar(50) not null,
mdp_utilisateur varchar(50) not null,
id_droit bigint(20) not null
);

create table employes (
id_employes bigint(20) primary key not null auto_increment,
nom_employe varchar(50) not null,
prenom_employe varchar(50) not null,
adresse_employe varchar(150) not null,
telephone_employe varchar(20) not null,
diplome_employe varchar(50),
annee_experience_employe date not null,
id_contrat bigint(20) not null,
id_equipe bigint(20) not null
);

create table contrat (
id_contrat bigint(20) primary key not null auto_increment,
employe_ou_interim_contrat varchar(20) not null
);

create table competence (
id_competence bigint(20) primary key not null auto_increment,
competence varchar(50)
);

create table equipe (
id_equipe bigint(20) primary key not null auto_increment,
nom_equipe varchar(50) not null
);

create table chaine_de_production (
id_chaine_de_production bigint(20) primary key not null auto_increment,
chaine_de_production varchar(50) not null
);

create table panne (
id_panne bigint(20) primary key not null auto_increment,
type_panne varchar(100) not null,
duree_panne time
);

create table moyen_reparation (
id_moyen_reparation bigint(20) primary key not null auto_increment,
achat_piece_reparation varchar(50) default null,
remplacement_logiciel_reparation varchar(50) default null,
autre_reparation varchar(50) default null,
id_panne bigint(20) not null
);

create table matiere_premiere (
id_matiere_premiere bigint(20) primary key not null auto_increment,
nom_mat_premiere varchar(50) not null,
type_mat_premiere varchar(50) not null
);

create table produit_fini (
id_produit_fini bigint(20) primary key not null auto_increment,
nom_produit_fini varchar(50) not null,
type_produit_fini varchar(50) not null,
duree_conservation_produit_fini date default null
);

alter table utilisateur
add constraint foreign key (id_droit) references droit (id_droit);

alter table employes
add constraint foreign key (id_contrat) references contrat (id_contrat),
add constraint foreign key (id_equipe) references equipe (id_equipe);

alter table moyen_reparation
add constraint foreign key (id_panne) references panne (id_panne);


CREATE TABLE savoir (
    id_employes BIGINT(20),
    id_competence BIGINT(20),
    PRIMARY KEY (id_employes , id_competence),
    FOREIGN KEY (id_employes)
        REFERENCES employes (id_employes),
    FOREIGN KEY (id_competence)
        REFERENCES competence (id_competence)
);

CREATE TABLE travailler (
    id_equipe BIGINT(20),
    id_chaine_de_production BIGINT(20),
    PRIMARY KEY (id_equipe , id_chaine_de_production),
    FOREIGN KEY (id_equipe)
        REFERENCES equipe (id_equipe),
    FOREIGN KEY (id_chaine_de_production)
        REFERENCES chaine_de_production (id_chaine_de_production)
);

CREATE TABLE recevoir (
    id_chaine_de_production BIGINT(20),
    id_matiere_premiere BIGINT(20),
    PRIMARY KEY (id_chaine_de_production , id_matiere_premiere),
    FOREIGN KEY (id_chaine_de_production)
        REFERENCES chaine_de_production (id_chaine_de_production),
    FOREIGN KEY (id_matiere_premiere)
        REFERENCES matiere_premiere (id_matiere_premiere)
);

CREATE TABLE produire (
    id_chaine_de_production BIGINT(20),
    id_produit_fini BIGINT(20),
    PRIMARY KEY (id_chaine_de_production , id_produit_fini),
    FOREIGN KEY (id_chaine_de_production)
        REFERENCES chaine_de_production (id_chaine_de_production),
    FOREIGN KEY (id_produit_fini)
        REFERENCES produit_fini (id_produit_fini)
);

CREATE TABLE subir (
    id_chaine_de_production BIGINT(20),
    id_panne BIGINT(20),
    PRIMARY KEY (id_chaine_de_production , id_panne),
    FOREIGN KEY (id_chaine_de_production)
        REFERENCES chaine_de_production (id_chaine_de_production),
    FOREIGN KEY (id_panne)
        REFERENCES panne (id_panne)
);

insert into droit (droit) values
('administrateur'),
('retrait'),
('reseau'),
('gerance');

insert into utilisateur (identifiant_utilisateur, mdp_utilisateur, id_droit) values
('micheldu31','1234','1'),
('reneedu92','5678','2'),
('pierredu11','9012','3'),
('lucasfilms','3456', '4');

insert into contrat (employe_ou_interim_contrat) values
('employe'),
("interimaire");

insert into equipe (nom_equipe) values
('les forts'),
('les nuls'),
('les a virer'),
('les toujours absent');


insert into employes (nom_employe, prenom_employe, adresse_employe, telephone_employe, diplome_employe, annee_experience_employe, id_contrat, id_equipe) values
('mimi',"michel", 'rue de michel', 0611111111, "diplome de michel", '1664-11-27', 1, 1),
('rere','renee', 'rue de renee', 0622222222, 'diplome de renee', '1111-01-01', 1, 1),
('pipi', 'pierre', 'rue de pierre', 0633333333, 'diplome de pierre', '214-05-24', 1, 2),
('lulu', 'lucas', 'rue de lucas', 0644444444, 'diplome de lucas', '1-01-01', 2,2);

insert into competence (competence) values
('compter 2 par 2'),
('lasser ses chaussures'),
('sauter a cloche pied'),
('gober un flan');

insert into chaine_de_production (chaine_de_production) values
('chaine des cures dents'),
('chaine des ongles de pieds'),
('chaine des fainéant'),
('chaine qui marche jamais'),
('chaine des mecs absents');

insert into panne (type_panne, duree_panne) values
('ca marche pas','838:59'),
('ca marche un peu', '400:12'),
('ca marche bien', '100:14:58'),
('ca marche super', '4:12');

insert into moyen_reparation (achat_piece_reparation, remplacement_logiciel_reparation, autre_reparation, id_panne) values
('clou'," "," ", 1 ),
(" ", "windows"," ", 2 ),
(" ", " ","michel qui tape au marteau", 3 ),
('vis'," "," ", 4);

insert into matiere_premiere (nom_mat_premiere, type_mat_premiere) values
("frene", "bois"),
("ongle", "matiere vivant"),
("silex","caillou"),
("rubis vert","rubis");

insert into produit_fini (nom_produit_fini, type_produit_fini, duree_conservation_produit_fini) values
("cure dent", "cureur de dent","2021-01-11"),
("ongle de pied plat", "ongle","2022-11-01"),
("statue de truc moche", "statue", "3145-01-01"),
("rien puisqu'il sont absent", "rien", " ");

insert into savoir (id_employes, id_competence) values
("1","1"),
("2","2"),
("3","3"),
("3","4");

insert into travailler (id_equipe, id_chaine_de_production) values
("1","1"),
("1","2"),
("2","3"),
("2","1");

insert into subir (id_chaine_de_production, id_panne) values
("4","1"),
("3","2"),
("2","3"),
("1","4");

insert into recevoir (id_chaine_de_production, id_matiere_premiere) values
("1","3"),

("2","4"),
("2","1");

insert into produire (id_chaine_de_production, id_produit_fini) values
("1","3"),
("1","2"),
("2","4"),
("2","1");




