from app.models.review import Review
from app.serializers.review_serializer import ReviewSerializer


class ReviewService:

    def get_all_reviews(self):
        reviews = Review.get_all_reviews()
        return ReviewSerializer(reviews, many=True).data

    def create_review(self, review_data):
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
