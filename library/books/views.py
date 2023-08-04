import json
import uuid
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .utils import save_log 
from .models import Book

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def books(request):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try: 
        books = Book.objects.all().values()
        books = list(book for book in books)
        json_response.update({
            'response_message': 'Get Books Succeeded.',
            'data': str(books),
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

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_book(request, id):
    json_response = {
        'response_id': str(uuid.uuid4().hex)
    }
    try: 
        book = Book.objects.get(id = id)
        json_response.update({
            'response_message': 'Get Book Succeeded.',
            'data': str(book),
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
    
@api_view(['POST'])
@renderer_classes([JSONRenderer])
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

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
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

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
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
            'response_message': 'Delete Book Failed',
            'error': str(e),
        })

        save_log(request, json_response)
        return Response(json_response, status = status.HTTP_417_EXPECTATION_FAILED)
