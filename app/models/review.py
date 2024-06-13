from django.db import models

from app.models.book import Book

from .base import BaseModel
from django.contrib.auth.models import User


class Review(BaseModel):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.content} - {self.book.title} by {self.user}"

    @classmethod
    def get_all_reviews(cls):
        return cls.objects.all()

    @classmethod
    def get_review_by_id(cls, id):
        try:
            return cls.objects.get(idx=id, is_deleted=False)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_review_for_book(cls, book_id):
        try:
            return cls.objects.filter(book__idx=book_id)
        except cls.DoesNotExist:
            return None
