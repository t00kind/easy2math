from django.shortcuts import render
from .models import Mm

def main(request):
    main = Mm.objects.all()
    title = "easy2math"
    return render(request, 'main/index.html', {'main': main, "title": title})