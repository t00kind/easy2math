from django.shortcuts import render
from .models import Books

def main(requests):
    bk = Books.objects.all()
    title = "Книги"
    return render(requests, '../templates/books/index.html', {'bk': bk, "title": title})
