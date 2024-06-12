from django.db import models

from .base import BaseModel
from django.contrib.auth.models import User


class Book(BaseModel):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to="cover_images/")
    author = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} - {self.author}"

    @classmethod
    def get_all_books(cls):
        return cls.objects.all()

    @classmethod
    def get_book_by_id(cls, id):
        try:
            return cls.objects.get(idx=id, is_deleted=False)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_book_by_title(cls, title):
        try:
            return cls.objects.get(title=title, is_deleted=False)
        except cls.DoesNotExist:
            return None
