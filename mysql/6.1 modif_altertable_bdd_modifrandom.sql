use usine_production;

#drop table utilisateur;

#alter table utilisateur
#drop foreign key utilisateur_ibfk_1;

#alter table droit
#add column aucun_droit varchar(50) default null;

#alter table droit
#drop column aucun_droit;

#alter table employes
#modify prenom_employe varchar(100);

#update employes
#set prenom_employe = "michou"
#where id_employes = 1;

#delete from moyen_reparation
#where autre_reparation = "michel qui tape au marteau";

#select * from employes;

#select nom_employe from employes;

#select distinct nom_employe from employes;

#select prenom_employe, nom_employe, competence from employes left join savoir on employes.id_employes= savoir.id_employes
#left join competence on savoir.id_competence=competence.id_competence;

#select chaine_de_production, nom_mat_premiere from chaine_de_production inner join recevoir on chaine_de_production.id_chaine_de_production = recevoir.id_chaine_de_production
#inner join matiere_premiere on recevoir.id_matiere_premiere = matiere_premiere.id_matiere_premiere;

#select chaine_de_production, nom_mat_premiere from chaine_de_production right join recevoir on chaine_de_production.id_chaine_de_production = recevoir.id_chaine_de_production
#right join matiere_premiere on recevoir.id_matiere_premiere = matiere_premiere.id_matiere_premiere;

#select count(nom_employe) from employes;

#select sum(duree_panne) from panne;
#-	Par chaine de production et par mois donner la durée totale de panne PAF FAIIITTT

#select prenom_employe, count(competence) from employes left join savoir on employes.id_employes = savoir.id_employes
#left join competence on savoir. id_competence = competence.id_competence group by prenom_employe;

#select nom_employe from employes where nom_employe between "l" and "n";














