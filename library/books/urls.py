from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<uuid:id>', views.get_book, name='get_book')
]