from django.urls import path
from . import views

app_name = 'AppGestion'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='logout'),
    path('registered/', views.registered, name='registered'),
    path('welcome/', views.welcome, name='welcome'),
    path('profil/', views.profil, name='profil'),
    path('profil/modifierProfil', views.modifierProfil, name='modifierProfil'),
    path('profil/modifierProfil/updateProfil', views.updateProfil, name='updateProfil'),
    path('profil/modifierProfil/supprimerProfil', views.supprimerProfil, name='supprimerProfil'),
    path('profil/modifierProfil/supprimerProfil/deleteProfil', views.deleteProfil, name='deleteProfil'),
    path('profil/become/', views.become, name='become'),
    path('profil/makeReservationSalle/', views.makeReservationSalle, name='makeReservationSalle'),
    path('profil/personalReservation/', views.personalReservation, name='personalReservation'),
    path('profil/addEvent/', views.addEvent, name='addEvent'),
    path('displayEvents/detailEvent/<int:evenement_id>/reservationBillet/', views.reservationBillet, name='reservationBillet'),
    path('displayEvents/detailEvent/<int:evenement_id>/reservationBillet/reservationBilletValide/', views.reservationBilletValide, name='reservationBilletValide'),
    path('displayEvents/detailEvent/<int:evenement_id>/', views.detailEvent, name='detailEvent'),
    path('displayEvents/', views.displayEvents, name='displayEvents'),
    path('displaySalles/', views.displaySalles, name='displaySalles'),
    path('displaySalles/detailSalle/<int:salle_id>/', views.detailSalle, name='detailSalle'),
    path('profil/detailTicket/<int:ticket_id>/', views.detailTicket, name='detailTicket'),
    path('profil/detailReservation/<int:reservation_id>/', views.detailReservation, name='detailReservation'),
]
