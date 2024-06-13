from rest_framework import serializers

from app.models.book import Book
from app.serializers.review_serializer import ReviewSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            "idx",
            "title",
            "cover_image",
            "author",
            "publication_date",
            "created_by",
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = [
            "idx",
            "title",
            "cover_image",
            "author",
            "publication_date",
            "created_by",
            "average_rating",
            "reviews",
        ]
