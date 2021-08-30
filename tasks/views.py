from django.shortcuts import render
from .models import Tt


def get(request):
    undo = Tt.objects.all()
    return render(request, 'tasks/index.html', {'undo': undo})