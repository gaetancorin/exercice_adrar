use exercice_ticket;

select * from ticket;
select ticket.id_ticket, prix_article*quantite_article from ticket inner join associer on ticket.id_ticket = associer.id_ticket 
inner join article on associer.id_article = article.id_article;
select nom_article, prix_article from ticket inner join associer on ticket.id_ticket = associer.id_ticket 
inner join article on associer.id_article = article.id_article where id_vendeur = 3;
select nom_vendeur, nom_article, prix_article, quantite_article, date_ticket from article inner join associer on article.id_article = associer.id_ticket inner join ticket on associer.id_ticket =ticket.id_ticket inner join vendeur on ticket.id_vendeur = vendeur.id_vendeur;
select nom_article from article inner join associer on article.id_article = associer.id_article inner join ticket on associer.id_ticket = ticket.id_ticket inner join vendeur on ticket.id_vendeur = vendeur.id_vendeur where date_ticket between "2021-06-01" and "2021-11-01" and vendeur.id_vendeur = 1 order by nom_article desc ;
#select nom_article from article inner join associer on article.id_article = associer.id_article inner join ticket on associer.id_ticket = ticket.id_ticket inner join vendeur on ticket.id_vendeur = vendeur.id_vendeur where vendeur.id_vendeur = 1 and date_ticket between "2021-06-01" and "2021-11-01" order by nom_article desc ;
select id_article, prix_article, avg(prix_article) as "prix_moyen" from article;
