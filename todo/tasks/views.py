from django.shortcuts import render, redirect

from .forms import *


def index(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def complete(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        if task:
            task.completed = True
            task.save()
            return redirect("/")


def update(request, task_id):
    pass


def delete(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
            return redirect("/")