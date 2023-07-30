import json
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Book

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def books(request):
    try: 
        books = Book.objects.all().values()
        books = list(book for book in books)
        json_response = {
            'response_id': '',
            'response_message': 'Get Books Success.',
            'data': str(books),
        }

        return Response(json_response, status=status.HTTP_200_OK)
    
    except Exception as e:
        json_response = {
            'response_id': '',
            'response_message': 'Get Books Failed.',
            'error': str(e)
        }
        return Response(json_response, status=status.HTTP_417_EXPECTATION_FAILED)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_book(request, id):
    try: 
        book = Book.objects.get(id = id)
        json_response = {
            'response_id': '',
            'response_message': 'Get Book Success.',
            'data': str(book),
        }

        return Response(json_response, status=status.HTTP_200_OK)
    
    except Exception as e:
        json_response = {
            'response_id': '',
            'response_message': 'Get Book Failed.',
            'error': str(e),
        }

        return Response(json_response, status=status.HTTP_417_EXPECTATION_FAILED)
    
@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_book(request):
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

        json_response = {
            'response_id': '',
            'response_message': 'Add Book Success.',
        }

        return Response(json_response, status=status.HTTP_200_OK)

    except Exception as e:
        json_response = {
            'response_id': '',
        }

        if type(e) == KeyError:
            json_response.update({
                'response_message': 'Error in Request Model.',
                'error': str(e),
            })

            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            json_response.update({
                'response_message': 'Add Book Failed.',
                'error': str(e),
            })
        
            return Response(json_response, status=status.HTTP_417_EXPECTATION_FAILED)
