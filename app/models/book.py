from django.db import models

from .base import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to="cover_images/")
    author = models.CharField(max_length=255)
    publication_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.author}"
    
