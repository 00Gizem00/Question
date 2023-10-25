import random
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from Questions.utils import is_phone_number_correct
from .models import Question, Answer, Score


def index(request):

    questions = Question.objects.all()


    return render(request, 'index.html', {'questions': questions})


def send_quiz(request):
    if request.method == 'GET':
        return redirect('/')
    
    return JsonResponse(request.POST)

    phone_correct = is_phone_number_correct(request.POST.get("Telefon", ""))

    score = 0
    max_score = 0

    wrong_answers = []

    Quiz.objects.all()