from django.db import models

from app.models.book import Book

from .base import BaseModel
from django.contrib.auth.models import User


class Review(BaseModel):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.content} - {self.book.title} by {self.user}"

    @classmethod
    def get_all_reviews(cls):
        return cls.objects.all()
