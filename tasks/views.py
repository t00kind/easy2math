from django.shortcuts import render
from .models import Task
from lessons.models import Tag


def get(request):
    undo = Task.objects.all()
    title = "Задачи"
    return render(request, 'tasks/index.html', {'undo': undo, "title": title})


def by_tag(request, tag_id):
    tgs = Task.objects.filter(tag=tag_id)
    tags = Tag.objets.all()
    current_tag = Tag.objects.get(pk=tag_id)
    context = {"tgs": tgs, "tags": tags, "current_tag": current_tag}
    return render(request, "task/by_tag.html", context)