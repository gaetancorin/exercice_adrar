import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Question, Citizen

# Create your tests here.
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_user_not_citizen(username, email, password):
    user = User.objects.create_user(username, email, password)
    return user

def create_user_citizen(user):
    citizen =Citizen(user=user)
    citizen.electeur = True
    citizen.save()
    return citizen

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False pour une question publiée dans le futur.
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_wad_published_recently_with_old_question(self):
        """
        was_published_recently() returns False pour les questions plus vieilles qu'un jour.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True pour les questions du jour.
        """
        time=timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class QuestionIndexviewTests(TestCase):
    def test_no_question(self):
        """
        Test de notre vue index si il n'y a pas de question
        """
        response = self.client.get(reverse('sondage:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pas de sondage disponible.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_question(self):
        """
        Test de notre vue index si la question a une date passé
        """
        question = create_question("Question passé", -10)
        response = self.client.get(reverse('sondage:index'))
        self.assertQuerysetEqual(response.context['question_list'], [question])

    def test_futur_question(self):
        """
        Test de notre vue index si la question a une date futur
        """
        create_question("Future question", 10)
        response = self.client.get(reverse('sondage:index'))
        self.assertContains(response, "Pas de sondage disponible.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_futur_and_past_question(self):
        question = create_question("Question passé", -2)
        create_question("Future question", 15)
        response = self.client.get(reverse('sondage:index'))
        self.assertQuerysetEqual(response.context['question_list'], [question])

    def test_multiple_past_questions(self):
        question1 = create_question("Première question passé", -5)
        question2 = create_question("Deuxième question passé", -6)
        response = self.client.get(reverse('sondage:index'))
        self.assertQuerysetEqual(response.context['question_list'], [question1, question2])

class QuestionDetailViewTests(TestCase):
    def test_futur_question(self):
        futur_question = create_question("Futur question", 8)
        url = reverse('sondage:detail', args=(futur_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        question = create_question("Question passé", -3)
        url = reverse('sondage:detail', args=(question.id,))

        user = create_user_not_citizen("Monsuperusername", "email@email.fr", "passworddu31")
        create_user_citizen(user)
        self.client.login(username="Monsuperusername", password="passworddu31")

        response = self.client.get(url)
        print(response.content)
        self.assertContains(response, question.question_text)

