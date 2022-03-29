from django.urls import path

from . import views
app_name = 'sondage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='logout'),
    path('registered/', views.registered, name='registered'),
    path('welcome/', views.welcome, name='welcome'),
    path('profil/', views.profil, name='profil'),
    path('profil/become', views.become, name='become'),
]
