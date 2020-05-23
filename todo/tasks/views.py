from django.shortcuts import render

from .forms import *


def index(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})