from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import random

import sqlite3

def get_count_cards():
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    sqlite_query = """SELECT MAX(id) FROM main_task"""
    cursor.execute(sqlite_query)
    count1 = cursor.fetchone()
    cursor.close()
    return count1[0]


def index(request):
    count = get_count_cards()

    if count != 0 and count is not None:
        tasks = Task.objects.get(id=random.randint(1, count))
    else:
        tasks = {'title': 'You have 0 cards. Please add it in Add Card menu', 'description':'Please go to Add Cards menu'}

    form = TaskForm(request.POST)

    return render(request, 'main/index.html', {'title': 'LVC - Mane page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html', {'title': 'LVC - About us'})

def add(request):
    info = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            info = 'Data was stored successful'
            form = TaskForm()
            context = {
                'form' : form,
                'info': info
            }
            return render(request, 'main/add.html', context)
        else:
            info = 'Form is unvalid!'


    form = TaskForm()
    context = {
        'form': form,
        'info': info
    }
    return render(request, 'main/add.html', context)


