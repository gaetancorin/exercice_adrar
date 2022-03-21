from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
# Create your views here.

from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': latest_question_list}
    return render(request, 'sondage/index.html', context)


class IndexViews(generic.ListView):
    template_name = 'sondage/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondage/detail.html', {'question':question})


class DetailViews(generic.DetailView):
    model = Question
    template_name = 'sondage/detail.html'


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

