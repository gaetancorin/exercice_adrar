from datetime import datetime
from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

class Salle(models.Model):
    nom = models.CharField(max_length=127)
    jauge_max_assise = models.IntegerField(default=0)
    jauge_max_debout = models.IntegerField(default=0)
    equipement_audio = models.BooleanField()
    equipement_lumiere = models.BooleanField()
    equipement_stand = models.BooleanField()
    equipement_rideau = models.BooleanField()

    def __str__(self):
        return self.nom

class Intervenant(models.Model):
    nom = models.CharField(max_length=127)

    def __str__(self):
        return self.nom

class TypeEvenement(models.Model):
    nom = models.CharField(max_length=127)

    def __str__(self):
        return self.nom

class ReservationSalle(models.Model):
    nom = models.CharField(max_length=127)
    date_debut = models.DateField(default=date.today)
    date_fin = models.DateField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Evenement(models.Model):
    nom = models.CharField(max_length=127)
    date_debut = models.DateField()
    date_fin = models.DateField()
    info = models.TextField(null=True, blank=True)
    illustration = models.ImageField(null=True, blank=True, upload_to='AppGestion\static\AppGestion\images\evenement')
    place_restante = models.IntegerField(null=True, blank=True)
    type_evenement = models.ForeignKey(TypeEvenement, on_delete=models.CASCADE, null=True, blank=True)
    ticket_achete = models.ManyToManyField(User, through='Asso9', blank=True)
    intervenant = models.ManyToManyField(Intervenant, blank=True)
    reservation = models.OneToOneField(ReservationSalle, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Asso9(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    nb_place_assise = models.IntegerField(default=0)
    nb_place_debout = models.IntegerField(default=0)

    def __str__(self):
        return f"user = {self.user} + event = {self.event}"

class Organisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisateur = models.BooleanField(default=False)





