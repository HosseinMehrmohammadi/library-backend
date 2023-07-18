import uuid
import datetime
from django.db import models

class Book(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(
        max_length = 255
    )
    author = models.CharField(
        max_length = 255
    )
    genre = models.CharField(
        max_length = 255,
        null = True
    )
    published_year = models.IntegerField(
        null = True   
    )
    is_available = models.BooleanField(
        default = False
    )
    created_at = models.DateField(
        default = datetime.datetime.now()
    )
