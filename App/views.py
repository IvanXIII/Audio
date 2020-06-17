from django.http import HttpResponse
from django.shortcuts import render

from App.forms import TaskForm
from App.models import Task, Lection


def tasks(request):
    if request.method == 'POST':
        new_task = Task()
        new_task.nickname = request.POST.get('nickname')
        new_task.feedback = request.POST.get('feedback')
        new_task.save()

    all_tasks = Task.objects.all()
    task_form = TaskForm()
    context = {'all_tasks': all_tasks, 'task_form': task_form}
    return render(request, 'App/tasks.html', context)

def home(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.short_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/home.html ', context)


def lections(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/lect.html ', context)

def lol(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/list_of_lect.html ', context)

def lect1(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/l1.html', context)

def lect2(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/l2.html', context)

def lect3(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/l3.html', context)

def lect4(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/l4.html', context)

def lect5(request):
    if request.method == 'POST':
        new_lection = Lection()
        new_lection.name = request.POST.get('name')
        new_lection.number_of_lection = request.POST.get('number_of_lection')
        new_lection.description = request.POST.get('description')
        new_lection.long_description = request.POST.get('short_description')
        new_lection.photo = request.POST.get('photo')
        new_lection.audio = request.POST.get('audio')
        new_lection.save()

    all_lections = Lection.objects.all()
    context = {'all_lections': all_lections}
    return render(request, 'App/l5.html', context)