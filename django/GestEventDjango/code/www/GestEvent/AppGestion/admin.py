from django.contrib import admin
from .models import Salle, Evenement, Intervenant, TypeEvenement, Organisateur, ReservationSalle, Asso9

# Register your models here.
admin.site.register(Salle)
admin.site.register(Evenement)
admin.site.register(Intervenant)
admin.site.register(TypeEvenement)
admin.site.register(Organisateur)
admin.site.register(ReservationSalle)
admin.site.register(Asso9)
