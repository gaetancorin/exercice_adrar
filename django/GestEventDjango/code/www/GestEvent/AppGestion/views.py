from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Salle, Intervenant, Evenement, TypeEvenement, Organisateur, ReservationSalle, Asso9
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


# Create your views here.
def index(request):
    # event_list = Evenement.objects.order_by('-id')[:5]
    # context = {'event_list': event_list}
    # return render(request, 'AppGestion/index.html', context)

    event_list = Evenement.objects.order_by('id')
    dico_event = {}
    for un_evenement in event_list:
        lien_image = str(un_evenement.illustration)[18:]
        dico_event[un_evenement] = lien_image
    context = {'event_list': event_list, 'event_image': dico_event}
    return render(request, 'AppGestion/index.html', context)

def my_login(request):
    return render(request, 'AppGestion/login.html')

def register(request):
    return render(request, 'AppGestion/register.html')

def my_logout(request):
    logout(request)
    return render(request, 'AppGestion/logout.html')

def registered(request):
    name = request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    organisateur = Organisateur(user=user)
    user.last_name = name
    user.first_name = firstname
    user.save()
    organisateur.save()
    context = {'user': user}
    return render(request, 'AppGestion/registered.html', context)

def welcome(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None:
        login(request, user)
        return render(request, 'AppGestion/welcome.html', context)
    else:
        return render(request, 'AppGestion/error_log.html')

def profil(request):
    organisateur = Organisateur.objects.get(user=request.user)
    list_ticket = Asso9.objects.order_by('id')
    list_reservation = ReservationSalle.objects.order_by('id')
    context = {'organisateur': organisateur,'list_ticket':list_ticket,'list_reservation': list_reservation}
    return render(request, 'AppGestion/profil.html', context)

def become(request):
    request.user.organisateur.organisateur = True
    request.user.organisateur.save()
    return render(request, 'AppGestion/profil.html')

def modifierProfil(request):
    return render(request, 'AppGestion/modifierProfil.html')

def updateProfil(request, ):
    email = request.POST['email']
    passwordOld = request.POST['passwordOld']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if len(email) != 0:
        request.user.email = email
        request.user.save()
    if len(passwordOld) != 0:
        if passwordOld == request.user.password:
            if password1 == password2:
                request.user.set_password(password1)
                request.user.save()
    return render(request, 'AppGestion/profil.html')

def supprimerProfil(request):
    return render(request, 'AppGestion/supprimerProfil.html')

def deleteProfil(request):
    request.user.delete()
    return render(request, 'AppGestion/index.html')

def displayEvents(request):
    event_list = Evenement.objects.order_by('id')
    dico_event = {}
    for un_evenement in event_list:
        lien_image = str(un_evenement.illustration)[18:]
        dico_event[un_evenement] = lien_image
    context = {'event_list': event_list, 'event_image': dico_event}
    return render(request, 'AppGestion/displayEvents.html', context)

def detailEvent(request, evenement_id):
    evenement = get_object_or_404(Evenement, pk=evenement_id)
    img = str(evenement.illustration)[18:]
    estValide = timezone.now().date() <= evenement.date_fin
    ventes = (evenement.reservation.salle.jauge_max_assise + evenement.reservation.salle.jauge_max_debout) - evenement.place_restante
    return render(request, 'AppGestion/detailEvent.html', {'evenement':evenement, 'img':img, 'validite':estValide, 'ventes': ventes})

def displaySalles(request):
    salle_list = Salle.objects.order_by('id')
    context = {'salle_list': salle_list}
    return render(request, 'AppGestion/displaySalles.html', context)

def detailSalle(request, salle_id):
    salle = get_object_or_404(Salle, pk=salle_id)
    return render(request, 'AppGestion/detailSalle.html', {'salle':salle})

def personalReservation(request):
    reservation_list = ReservationSalle.objects.filter(utilisateur=request.user)
    contexte = {'reservation_list': reservation_list}
    return render(request, 'AppGestion/personalReservation.html', contexte)

def reservationBillet(request, evenement_id):
    event = Evenement.objects.get(pk=evenement_id)
    return render(request, 'AppGestion/reservationBillet.html', {'event':event})

def reservationBilletValide(request, evenement_id):
    event = Evenement.objects.get(pk=evenement_id)
    assis = int(request.POST['nb_place_assise'])
    debout = int(request.POST['nb_place_debout'])
    try:
        billet = Asso9.objects.get(event=event, user=request.user)
    except Asso9.DoesNotExist :
        event.ticket_achete.add(request.user)
        billet = Asso9.objects.get(event=event, user=request.user)
    finally:
        billet.nb_place_assise += assis
        billet.nb_place_debout += debout
        billet.save()
        event.place_restante -= (assis + debout)
        event.save()
    context = {'event': event, 'billet':billet}
    return render(request, 'AppGestion/reservationBilletValide.html', context)

def makeReservationSalle(request):
    return render(request, 'AppGestion/makeReservationSalle.html')

def addEvent(request):
    name = request.POST['event_name']
    begin = request.POST['date_debut']
    end = request.POST['date_fin']
    info = request.POST['info_event']
    illustration = request.POST['illustration_event']
    # place restante
    # request info utilisateur
    return render(request, 'AppGestion/addEvent.html')

def detailTicket(request, ticket_id):
    ticket = get_object_or_404(Asso9, pk=ticket_id)
    return render(request, 'AppGestion/detailTicket.html', {'ticket':ticket})

def detailReservation(request, reservation_id):
    reservation = get_object_or_404(ReservationSalle, pk=reservation_id)
    return render(request, 'AppGestion/detailReservation.html', {'reservation':reservation})
