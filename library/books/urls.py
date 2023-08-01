from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<uuid:id>', views.get_book, name='get_book'),
    path('add', csrf_exempt(views.add_book), name='add_book'),
    path('<uuid:id>/update', views.update_book, name='update_book')
]