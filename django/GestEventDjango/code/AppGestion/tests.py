import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Salle, Intervenant, Evenement, TypeEvenement, Organisateur, ReservationSalle, Asso9

# Create your tests here.
def create_user_not_organisateur(username, email, password):
    user = User.objects.create_user(username, email, password)
    return user
def create_organisateur(user):
    orga = Organisateur(user=user)
    orga.organisateur = True
    orga.save()
    return orga
def create_salle(nom, jauge_max_assise, jauge_max_debout, equipement_audio, equipement_lumiere, equipement_stand, equipement_rideau):
    salletest = Salle(nom=nom, jauge_max_assise=jauge_max_assise, jauge_max_debout=jauge_max_debout, equipement_audio=equipement_audio, equipement_lumiere=equipement_lumiere, equipement_stand=equipement_stand, equipement_rideau=equipement_rideau)
    salletest.save()
    return salletest
def create_salle_full():
    salletest = Salle(nom="nomSalle", jauge_max_assise="50", jauge_max_debout="50", equipement_audio=True, equipement_lumiere=True, equipement_stand=True, equipement_rideau=False)
    salletest.save()
    return salletest
def create_intervenant(nom):
    interv = Intervenant(nom=nom)
    return interv
def create_type_evenement(nom):
    typeevent = TypeEvenement(nom=nom)
    typeevent.save()
    return typeevent
def create_reservation_salle(nom, date_debut, date_fin, user, salle):
    reservsalle = ReservationSalle(nom=nom, date_debut=date_debut, date_fin=date_fin, utilisateur=user, salle=salle)
    reservsalle.save()
    return reservsalle
def create_reservation_salle_full():
    nom = "NomReservationSalle"
    date_debut = timezone.now() + datetime.timedelta(days=30)
    date_fin = timezone.now() + datetime.timedelta(days=45)
    user = create_user_not_organisateur("nomUser", "email@email.fr", "password")
    create_organisateur(user)
    salle = create_salle_full()
    reserv_salle = ReservationSalle(nom=nom, date_debut=date_debut, date_fin=date_fin, utilisateur=user, salle=salle)
    reserv_salle.save()
    return reserv_salle
def create_evenement(nom, date_debut, date_fin, info, illustration, place_restante, type_evenement, reservation):
    event = Evenement(nom=nom, date_debut=date_debut, date_fin=date_fin, info=info, illustration=illustration, place_restante=place_restante, type_evenement=type_evenement, reservation=reservation)
    event.save()
    return event
def create_evenement_full():
    nom = "NomEvent"
    date_debut_event = timezone.now() + datetime.timedelta(days=35)
    date_fin_event = timezone.now() + datetime.timedelta(days=40)
    info = "Ceci représente les infos"
    illustration = "https://www.cdiscount.com/pdt2/5/6/9/1/700x700/tup4251898900569/rw/tupperware-pichet-frigo-350-ml-rose-avec-cadeau.jpg"
    place_restante = 200
    type_evenement = create_type_evenement("typeEvent")
    reservation = create_reservation_salle_full()

    event = Evenement(nom=nom, date_debut=date_debut_event, date_fin=date_fin_event, info=info, illustration=illustration,
                      place_restante=place_restante, type_evenement=type_evenement, reservation=reservation)
    event.save()
    return event

class connection(TestCase):
    def test_connection_user(self):
        """
        Test de la vue "index" qui retourne un paragraphe lorsqu'un user est connecté
        """
        user = create_user_not_organisateur("nomUser", "email@email.fr", "password")
        self.client.login(username="nomUser", password="password")
        response = self.client.get(reverse('AppGestion:index'))
        self.assertContains(response, "Vous pouvez désormais réserver des Billets !")

    def test_deconnection_user(self):
        """
        Test de la vue "index" qui retourne un paragraphe lorsque aucun user s'est connecté puis déconnecter
        """
        user = create_user_not_organisateur("nomUser", "email@email.fr", "password")
        self.client.login(username="nomUser", password="password")
        self.client.logout()
        response = self.client.get(reverse('AppGestion:index'))
        self.assertContains(response, "Connecter ou inscriver vous pour pouvoir réserver des Billets !")

    def test_organisateur_true(self):
        """
        Test de la vue "profil" qui retourne la réservation de salle lorsque un user connecté est organisateur en True
        """
        user = create_user_not_organisateur("nomUser", "email@email.fr", "password")
        self.client.login(username="nomUser", password="password")
        create_organisateur(user)
        response = self.client.get(reverse('AppGestion:profil'))
        self.assertContains(response, "Réserver une salle")

class creation_table_bdd(TestCase):
    def test_creation_salle(self):
        """
        test de création sur la BDD du model "Salle"
        ce test utilise les fonctions:
        create_salle()
        """
        nom = "nomSalle"
        jauge_max_assise = "50"
        jauge_max_debout = "50"
        equipement_audio = True
        equipement_lumiere = True
        equipement_stand = True
        equipement_rideau = False
        salle = create_salle(nom, jauge_max_assise, jauge_max_debout, equipement_audio, equipement_lumiere, equipement_stand, equipement_rideau)
        self.assertEqual(salle.nom, nom)
        self.assertEqual(salle.jauge_max_assise, jauge_max_assise)
        self.assertEqual(salle.equipement_rideau, equipement_rideau)

    def test_creation_salle_full(self):
        """
        test de création sur la BDD du model "Salle"
        ce test utilise les fonctions:
        create_salle_full()
        """
        salle = create_salle_full()
        self.assertEqual(salle.nom, "nomSalle")
        self.assertEqual(salle.jauge_max_assise, "50")
        self.assertEqual(salle.equipement_rideau, False)

    def test_creation_intervenant(self):
        """
        test de création sur la BDD du model "Intervenant"
        ce test utilise les fonctions:
        create_intervenant()
        """
        nom ="nomIntervenant"
        intervenant = create_intervenant(nom)
        self.assertEqual(intervenant.nom, nom)

    def test_creation_type_evenement(self):
        """
        test de création sur la BDD du model "TypeEvenement"
        ce test utilise les fonctions:
        create_type_evenement()
        """
        nom ="nomTypeEvenement"
        type_evenement = create_type_evenement(nom)
        self.assertEqual(type_evenement.nom, nom)

    def test_creation_reservation_salle(self):
        """
        test de création sur la BDD du model "ReservationSalle"
        ce test utilise les fonctions:
        create_user_not_organisateur()
        create_organisateur()
        create_salle_full()
        create_reservation_salle()
        """
        nom = "nomReservationSalle"
        date_debut = timezone.now() + datetime.timedelta(days=30)
        date_fin = timezone.now() + datetime.timedelta(days=45)
        user = create_user_not_organisateur("nomUser", "email@email.fr", "password")
        create_organisateur(user)
        salle = create_salle_full()
        reserv_salle = create_reservation_salle(nom, date_debut, date_fin, user, salle)
        self.assertEqual(reserv_salle.nom, nom)
        self.assertEqual(str(reserv_salle.utilisateur), user.username)
        self.assertEqual(str(reserv_salle.salle), salle.nom)

    def test_creation_reservation_salle_full(self):
        """
        test de création sur la BDD du model "ReservationSalle"
        ce test utilise les fonctions:
        create_reservation_salle_full()
        ( qui utilise
        create_user_not_organisateur()
        create_organisateur()
        create_salle_full() )
        """
        reserv_salle = create_reservation_salle_full()
        self.assertEqual(reserv_salle.nom, "NomReservationSalle")
        self.assertEqual(str(reserv_salle.utilisateur), "nomUser")
        self.assertEqual(str(reserv_salle.salle), "nomSalle")

    def test_creation_evenement(self):
        """
        test de création sur la BDD du model "Evenement"
        ce test utilise les fonctions:
        create_type_evenement()
        create_reservation_salle_full()
        ( qui utilise
        create_user_not_organisateur()
        create_organisateur()
        create_salle_full() )
        create_evenement()
        """
        nom = "NomEvent"
        date_debut_event = timezone.now() + datetime.timedelta(days=35)
        date_fin_event = timezone.now() + datetime.timedelta(days=40)
        info = "Ceci représente les infos"
        illustration = "https://www.cdiscount.com/pdt2/5/6/9/1/700x700/tup4251898900569/rw/tupperware-pichet-frigo-350-ml-rose-avec-cadeau.jpg"
        place_restante = 200
        type_evenement = create_type_evenement("typeEvent")
        reservation = create_reservation_salle_full()

        event = create_evenement(nom, date_debut_event, date_fin_event, info, illustration, place_restante, type_evenement, reservation)

        self.assertEqual(event.nom, nom)
        self.assertEqual(event.info, info)
        self.assertEqual(event.illustration, illustration)
        self.assertEqual(event.type_evenement.nom, type_evenement.nom)
        self.assertEqual(event.reservation.nom, reservation.nom)

    def test_creation_evenement_full(self):
        """
        test de création sur la BDD du model "Evenement"
        ce test utilise les fonctions:
        create_type_evenement()
        create_evenement()
        create_reservation_salle_full()
        ( qui utilise
        create_user_not_organisateur()
        create_organisateur()
        create_salle_full()
        )
        """
        event = create_evenement_full()
        self.assertEqual(event.nom, "NomEvent")
        self.assertEqual(event.info, "Ceci représente les infos")
        self.assertEqual(event.place_restante, 200)

    def test_table_association_intervenant_evenement(self):
        """
        test de la table d'association de la BDD entre "Intervenant" et "Evenement"
        ce test utilise les fonctions:
        create_evenement_full()
        ( qui utilise
        create_type_evenement()
        create_evenement()
        create_reservation_salle_full()
        ( qui utilise
        create_user_not_organisateur()
        create_organisateur()
        create_salle_full()
         ))
        """
        event = create_evenement_full()
        intervenant1 = Intervenant(nom="nomIntervenant1")
        intervenant1.save()
        intervenant2 = Intervenant(nom="nomIntervenant2")
        intervenant2.save()
        event.intervenant.add(intervenant1)
        event.intervenant.add(intervenant2)

        self.assertIn(intervenant1.nom, str(event.intervenant.all()))
        self.assertIn(intervenant2.nom, str(event.intervenant.all()))

    def test_table_association_user_evenement(self):
        """
        test dans la BDD de la table d'association "Asso9" entre la table "user" et "Evenement"
        ce test utilise les fonctions:
        create_user_not_organisateur()
        create_evenement_full()
        ( qui utilise
         create_type_evenement()
        create_evenement()
        create_reservation_salle_full()
        ( qui utilise
        create_user_not_organisateur()
        create_organisateur()
        create_salle_full()
        )
        )
        """
        user = create_user_not_organisateur("nomUser2", "email2@email.fr", "password")
        event = create_evenement_full()

        event.ticket_achete.add(user)
        self.assertIn(user.username, str(event.ticket_achete.all()))

class affichage_views(TestCase):

    def test_creation_salle_affichage_displaySalles(self):
        """
        Test de notre vue "displaySalles" qui fait apparaitre le nom de la salle quand celui-ci est créer
        L'utilisateur n'est pas connecté
        """
        salle = create_salle_full()
        response = self.client.get(reverse('AppGestion:displaySalles'))
        self.assertContains(response, salle.nom)

    def test_creation_salle_affichage_detailSalle(self):
        """
        Test de notre vue "displaySalles" qui fait apparaitre le nom de la salle quand celui-ci est créer
        L'utilisateur n'est pas connecté
        """
        salle = create_salle_full()
        response = self.client.get(reverse('AppGestion:detailSalle', args=(salle.id,)))
        self.assertContains(response, salle.nom)
        self.assertContains(response, salle.jauge_max_assise)
        self.assertContains(response, salle.jauge_max_debout)

    def test_creation_event_affichage_displayEvents(self):
        """
        test de la vue "displayEvents" qui fait apparaitre le nom de l'evenement quand celui-ci est créer
        L'utilisateur n'est pas connecté
        """
        event = create_evenement_full()
        response = self.client.get(reverse('AppGestion:displayEvents'))
        self.assertContains(response, event.nom)
        self.assertContains(response, event.info)

    def test_creation_event_affichage_detailEvent(self):
        """
        test de la vue "detailEvent" qui fait apparaitre le nom de l'evenement quand celui-ci est créer
        L'utilisateur n'est pas connecté
        """
        event = create_evenement_full()

        intervenant1 = Intervenant(nom="Miel Pops")
        intervenant1.save()
        intervenant2 = Intervenant(nom="Chocapic")
        intervenant2.save()
        event.intervenant.add(intervenant1)
        event.intervenant.add(intervenant2)

        response = self.client.get(reverse('AppGestion:detailEvent', args=(event.id,)))
        self.assertContains(response, event.nom)
        self.assertContains(response, event.info)

