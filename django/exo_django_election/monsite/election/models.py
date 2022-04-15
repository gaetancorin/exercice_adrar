from django.db import models

# Create your models here.

class Marque(models.Model):
    titre_marque = models.CharField(max_length=100)
    lien_photo_marque = models.CharField(max_length=1000)
    description_marque = models.CharField(max_length=2000)
    nombre_votes_marque = models.IntegerField(default=0)

    def __str__(self):
        return self.titre_marque

class Boisson(models.Model):
    titre_boisson = models.CharField(max_length=200)
    lien_photo_boisson = models.CharField(max_length=1000)
    description_boisson = models.CharField(max_length=2000)
    nombre_votes_boisson = models.IntegerField(default=0)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre_boisson
