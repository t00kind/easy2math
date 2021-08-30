from django.shortcuts import render
from .models import Mm


def booking(request):
    bk = Mm.objects.all()
    return render(request, 'books/index.html', {'bk': bk})
