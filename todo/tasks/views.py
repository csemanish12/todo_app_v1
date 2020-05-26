from django.shortcuts import render, redirect

from .forms import *


def index(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            task.completed = False
            task.save()
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def complete(request, task_id):
    payload = request.POST.dict()
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        if payload.get('box') == 'complete':
            task.completed = True
        else:
            task.completed = False
        task.save()
        return redirect("/")


def update(request, task_id):
    payload = request.POST.dict()
    task = Task.objects.get(id=task_id)
    if task:
        task.title = payload.get('title')
        task.save()
        return redirect("/")


def delete(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
            return redirect("/")