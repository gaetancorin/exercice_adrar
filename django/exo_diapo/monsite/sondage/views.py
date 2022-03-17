from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': latest_question_list}
    return render(request, 'sondage/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondage/detail.html', {'question':question})

def results(request, question_id):
    response = "Voici les votes de la question de la question numéro %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question numéro %s." % question_id)
