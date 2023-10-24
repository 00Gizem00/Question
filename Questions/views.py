from itertools import count
import random
from tkinter import scrolledtext
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from Questions.utils import is_phone_number_correct

# Create your views here.

questions = [
    {
        'id': 1,
        'Question': 'Aşağıdakilerden hangisi bir işletim sistemidir?',
        'correct_answer': 'Windows',
        'options': ['Windows', 'Word', 'Excel', 'Paint']
    },
    {
        'id': 2,
        'Question':'Arjantinin geçmişte İngiltere ile anlaşmazlık yaşadığı adalar hangisidir?',
        'correct_answer': 'Cayman Adaları',
        'options': ['Falkland Adaları','Cayman Adaları', 'Galapagos Adaları', 'Malvinler'],
    },
    {
        'id': 3,
        'Question':'Avustralyanın başkenti nedir?',
        'correct_answer':'Canberra',
        'options': ['Adelaide', 'Canberra', 'Sydney', 'Melbourne'],
    },
    {
        'id': 4,
        'Question':'Nauru hangi kıtadadır?',
        'correct_answer':'Okyanusya',
        'options': ['Okyanusya', 'Güney Amerika', 'Afrika', 'Kuzey Amerika'],
    },
    {
        'id': 5,
        'Question':'Aşağıdakilerden hangisi ....?',
        'correct_answer': '??',
        'options': ['!!', '..', '??', '%'],
    },
]

def index(request):

    for question in questions:
        random.shuffle(question['options'])


    return render(request, 'index.html', {'questions':questions})


def send_quiz(request):
    if request.method == 'GET':
        return redirect('/')
    
    phone_correct = is_phone_number_correct(request.POST.get('Telefon'))
    
    return HttpResponse(phone_correct)
    score = 0
    point = 100 / len(questions)

    wrong_answers = []

    for question in questions:
        if request.POST.get('Question' + str(question['id']), '') == question['correct_answer']:
            score += point
        else: 

            wrong_answers.append ({
                'Question': question['Question'],
                'correct_answer': question['correct_answer'],
            })
                
    
    return render(request, 'quiz_sonuc.html', {'score': score, 'wrong_answers': wrong_answers, 'phone_correct': phone_correct})