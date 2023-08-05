import uuid
from django.db import models

class Book(models.Model):
    def __str__(self):
        return f'{self.title}'

    def get_short_details(self):
        details = {
            'id': str(self.id),
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
        }
        
        return details

    def get_full_details(self):
        details = {
            'id': str(self.id),
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'published_year': self.published_year,
            'is_available': self.is_available,
            'created_at': str(self.created_at),
        }

        return details

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    title = models.CharField(
        max_length = 255,
    )
    author = models.CharField(
        max_length = 255,
    )
    genre = models.CharField(
        max_length = 255,
        null = True,
    )
    published_year = models.IntegerField(
        null = True,  
    )
    is_available = models.BooleanField(
        default = False,
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        editable = False,
    )
