from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    # path('', views.get_books, name='get_books'),
    path(
        '', 
        views.all_book_service, 
        name='all_book_service'
    ),
    path(
        '<uuid:id>',
        views.book_service, 
        name='book_service'
    ),
    # path('<uuid:id>', views.update_book, name='update_book'),
    # path('<uuid:id>', views.delete_book, name='delete_book'),
]