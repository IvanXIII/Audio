from django.http import HttpResponse
from django.shortcuts import render

from App.forms import TaskForm
from App.models import Task


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


def lections(request):
    return render(request, 'App/lections.html')

def home(request):
    return render(request, 'App/home.html')



