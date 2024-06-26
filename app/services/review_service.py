from app.models.review import Review
from app.serializers.review_serializer import ReviewSerializer
from django.core.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination


class ReviewListPagination(PageNumberPagination):
    page_size = 3


class ReviewService:

    def get_all_reviews(self,request):
        reviews = Review.get_all_reviews()
        paginator = ReviewListPagination()
        paginated_queryset = paginator.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(paginated_queryset, many=True)
        page_info = {
            "count": paginator.page.paginator.count,
            "page": paginator.page.number,
            "pages": paginator.page.paginator.num_pages,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
        }
        return serializer.data, page_info

    def create_review(self, review_data):
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    def get_review_by_id(self, id):
        review = Review.get_review_by_id(id=id)
        if not review:
            return None
        return ReviewSerializer(review).data

    def get_reviews_for_book(self, book_id):
        reviews = Review.get_review_for_book(book_id=book_id)
        if not reviews:
            return None
        return ReviewSerializer(reviews, many=True).data

    def update_review(self, review_id, data, user):
        review = Review.get_review_by_id(id=review_id)
        if not review:
            return None, "Review not Found"
        if review.user != user:
            raise PermissionDenied("You do not have permission to edit this review.")
        serializer = ReviewSerializer(review, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    def delete_review(self, review_id, user):
        review = Review.get_review_by_id(id=review_id)
        if not review:
            return None, "Review not Found"
        if review.user != user:
            raise PermissionDenied("You do not have permission to edit this review.")
        if not review:
            return False
        review.delete()
        return True
