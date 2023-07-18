import json
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

def add_book(request):
    book = json.loads(request.body)
    new_book = Book(
        title = book['title'],
        author = book['author'],
        genre = 
            book['genre'] 
            if 'genre' in book 
            else None,
        published_year = 
            book['published_year'] 
            if 'published_year' in book 
            else None,
        is_available = 
            book['is_available'] 
            if 'is_available' in book 
            else False,
    )
    new_book.save()
    
    return HttpResponse('add book success')
