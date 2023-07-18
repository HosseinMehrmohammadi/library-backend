from django.http import HttpResponse
from django.template import loader
from .models import Book

def books(request):
    books = Book.objects.all().values()
    template = loader.get_template('books.html')
    context = {
        'books': books,
    }

    return HttpResponse(template.render(context, request))

def get_book(request, id):
    book = Book.objects.get(id = id)
    template = loader.get_template('book.html')
    context = {
        'book': book,
    }

    return HttpResponse(template.render(context, request))