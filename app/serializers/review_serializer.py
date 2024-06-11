from rest_framework import serializers

from app.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["idx", "content", "user"]
