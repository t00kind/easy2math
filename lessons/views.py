from django.shortcuts import render
from .models import Ll


def index(request):
    sudo = Ll.objects.all()
    return render(request, 'tasks/index.html', {'sudo': sudo})