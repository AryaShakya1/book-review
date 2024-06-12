from rest_framework import serializers

from app.models.book import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["idx", "title", "cover_image", "author", "publication_date","created_by"]
