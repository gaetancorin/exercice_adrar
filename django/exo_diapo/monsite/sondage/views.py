from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Citizen
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
# Create your views here.

from django.template import loader


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'question_list': latest_question_list}
#     return render(request, 'sondage/index.html', context)


class IndexView(generic.ListView):
    template_name = 'sondage/index.html'
    context_object_name = 'question_list'

    # def get_queryset(self):
    #     return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'sondage/detail.html', {'question':question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'sondage/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondage/results.html', {'question':question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'sondage/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'sondage/detail.html', {'question': question, 'error_message': 'Vous devez choisir!',})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('sondage:results', args=(question_id,)))

def my_login(request):
    return render(request, 'sondage/login.html')

def register(request):
    return render(request, 'sondage/register.html')

def my_logout(request):
    logout(request)
    return render(request, 'sondage/logout.html')

def registered(request):
    name= request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    citizen = Citizen(user=user)
    user.last_name = name
    user.first_name = firstname
    user.save()
    citizen.save()
    context = {'user':user}
    return render(request, 'sondage/registered.html', context)

def welcome(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None:
        login(request, user)
        return render(request, 'sondage/welcome.html', context)
    else:
        return render(request, 'sondage/error_log.html')

def my_logout(request):
    logout(request)
    return render(request, 'sondage/logout.html')

def profil(request):
    citizen = Citizen.objects.get(user=request.user)
    context = {'citizen':citizen}
    return render(request, 'sondage/profil.html', context)

def become(request):
    request.user.citizen.electeur =True
    request.user.citizen.save()
    return IndexView.as_view()(request)



