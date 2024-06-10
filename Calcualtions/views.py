from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Calcualtions.serializers import *
from rest_framework import generics
import random

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class TrainingList(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class TrainingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

def show_registr(request):
    if request.method == 'post':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        url = "http://localhost:8000/user/"
        response = requests.post(url, data={
            'username': username,
            'lastname': lastname,
            'firstname': firstname,
            'email': email,
            'password': password,
        })
        if response.status_code == 201:
            print('Пользователь успешно создан.')
        else:
            print('Ошибка при создании пользователя. Код состояния:', response.status_code)
    return render(request, 'registr.html')

def index(request):
    if request.method == 'POST':
        return redirect('testLevel')
    return render(request, 'index.html')

def testLevel(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
    return render(request, 'testLevel.html')

def generate_example(request):
    level = request.GET.get('difficulty')
    type = request.GET.get('type_check')

    if level is None or level == '':
        level = 'easy'

    if type is None or type == '':
        type = 'addition'

    difficulty = 10
    if level == 'medium':
        difficulty = 100
    elif level == 'hard':
        difficulty = 1000


    operand1 = random.randint(1, difficulty)
    operand2 = random.randint(1, difficulty)
    answer = None

    if type == 'addition':
        answer = operand1 + operand2
        type = '+'
    elif type == 'subtraction':
        answer = operand1 - operand2
        type = '-'
    elif type == 'multiplication':
        answer = operand1 * operand2
        type = '*'
    elif type == 'division':
        if operand2 != 0:
            answer = operand1 / operand2
            type = '//'

    example = Problem(problem=f'{operand1} {type} {operand2}', answer=answer, type_problem=type, level=level, score=10)
    example.save()

    context = {
        'example': example,
    }
    return render(request, 'testLevel.html', context)

def check_answer(request):
    example_problem = request.GET.get('example_problem')
    answer = int(request.GET.get('answer'))

    example = Problem.objects.get(problem=example_problem)

    is_correct = False
    if int(example.answer) == answer:
        is_correct = True

    context = {
        'example': example,
        'is_correct': is_correct,
    }
    return render(request, 'testLevel.html', context)

def diffSettings(request):
    return render(request, 'settings.html')


