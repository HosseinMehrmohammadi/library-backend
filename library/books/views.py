import json
import uuid
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .utils import save_log 
from .models import Book

@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def all_book_service(request):
    if request.method == 'GET':
        return get_books(request)

    elif request.method == 'POST':
        return add_book(request)

### ------------------------------------------------------------- ###

@api_view(['GET', 'PUT', 'DELETE'])
@renderer_classes([JSONRenderer])
def book_service(request, id):
    if request.method == 'GET':
        return get_book(request, id)

    elif request.method == 'PUT':
        return update_book(request, id)

    elif request.method == 'DELETE':
        return delete_book(request, id)

### ------------------------------------------------------------- ###

def get_books(request):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try: 
        books = Book.objects.all()
        books = list(book.get_short_details() for book in books)
        json_response.update({
            'response_message': 'Get Books Succeeded.',
            'data': books,
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_200_OK)
    
    except Exception as e:
        json_response.update({
            'response_message': 'Get Books Failed.',
            'error': str(e),
        })
        
        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_417_EXPECTATION_FAILED)

### ------------------------------------------------------------- ###

def get_book(request, id):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try: 
        book = Book.objects.get(id = id).get_full_details()
        json_response.update({
            'response_message': 'Get Book Succeeded.',
            'data': book,
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_200_OK)
    
    except Exception as e:
        json_response.update({
            'response_message': 'Get Book Failed.',
            'error': str(e),
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_417_EXPECTATION_FAILED)
    
### ------------------------------------------------------------- ###

def add_book(request):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try:
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

        json_response.update({
            'response_message': 'Add Book Succeeded.',
        })
        
        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_200_OK)

    except Exception as e:
        if type(e) == KeyError:
            json_response.update({
                'response_message': 'Error in Request Model.',
                'error': str(e),
            })
            
            save_log(request, json_response)
            return Response(json_response, status = status.HTTP_400_BAD_REQUEST)
        
        else:
            json_response.update({
                'response_message': 'Add Book Failed.',
                'error': str(e),
            })
        
            save_log(request, json_response)
            return Response(json_response, status = status.HTTP_417_EXPECTATION_FAILED)

### ------------------------------------------------------------- ###

def update_book(request, id):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try:
        book = json.loads(request.body)
        updated_book = Book.objects.get(id = id)
        updated_book.title = book['title'] if 'title' in book else updated_book.title
        updated_book.author = book['author'] if 'author' in book else updated_book.author
        updated_book.genre = book['genre'] if 'genre' in book else updated_book.genre
        updated_book.published_year = book['published_year'] if 'published_year' in book else updated_book.published_year        
        updated_book.is_available = book['is_available'] if 'is_available' in book else updated_book.is_available
        updated_book.save()

        json_response.update({
            'response_message': 'Update Book Succeeded.',
        })
        
        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_200_OK)
    
    except Exception as e:
        json_response.update({
            'response_message': 'Update Book Failed.',
            'error': str(e),
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_417_EXPECTATION_FAILED)

### ------------------------------------------------------------- ###

def delete_book(request, id):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try:
        deleted_book = Book.objects.get(id = id)
        deleted_book.delete()

        json_response.update({
            'response_message': 'Delete Book Succeeded.',
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_200_OK)
    
    except Exception as e:
        json_response.update({
            'response_message': 'Delete Book Failed.',
            'error': str(e),
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_417_EXPECTATION_FAILED)
