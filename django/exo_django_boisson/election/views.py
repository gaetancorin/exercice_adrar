from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Marque, Boisson

# Create your views here.
def index(request):
    listeBoisson = Boisson.objects.order_by('-nombre_votes_boisson')
    template = loader.get_template('election/index.html')
    context = {'liste_boisson': listeBoisson}
    return HttpResponse(template.render(context, request))

def afficherBoisson(request, titre_boisson):
    return HttpResponse("Voici les informations de %s" % titre_boisson)
