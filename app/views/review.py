from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.builders.response_builder import ResponseBuilder
from app.services.review_service import ReviewService
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.core.exceptions import PermissionDenied


class ReviewView(APIView):

    def get_authenticators(self):
        if self.request.method == "POST":
            return [JWTAuthentication()]
        return [SessionAuthentication(), BasicAuthentication()]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            review_service = ReviewService()
            reviews = review_service.get_all_reviews()
            return (
                response_builder.result_object(reviews)
                .success()
                .ok_200()
                .get_response()
            )
        except Exception as e:
            print(f"ReviewView get :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to get reviews"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )

    def post(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            review_service = ReviewService()
            review_data = request.data.copy()
            review_data["user"] = request.user.id
            review, errors = review_service.create_review(review_data)
            if review:
                return (
                    response_builder.result_object(review)
                    .success()
                    .ok_200()
                    .get_response()
                )
            return (
                response_builder.result_object({"message": errors})
                .fail()
                .bad_request_400()
                .message("Bad Request")
                .get_response()
            )
        except Exception as e:
            print(f"ReviewView post :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to create review"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )


class ReviewUpdateDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, review_id):
        response_builder = ResponseBuilder()
        try:
            review_service = ReviewService()
            review_data = request.data
            review, errors = review_service.update_review(
                review_id, review_data, request.user
            )
            if review:
                return (
                    response_builder.result_object(review)
                    .success()
                    .ok_200()
                    .get_response()
                )
            return (
                response_builder.result_object({"message": errors})
                .fail()
                .bad_request_400()
                .message("Bad Request")
                .get_response()
            )
        except PermissionDenied:
            return (
                response_builder.fail()
                .user_forbidden_403()
                .message("Cannot edit other reviews")
                .get_response()
            )
        except Exception as e:
            print(f"ReviewUpdateDeleteView put :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to update review"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )

    def delete(self, request, review_id):
        response_builder = ResponseBuilder()
        try:
            review_service = ReviewService()
            success = review_service.delete_review(review_id, request.user)
            if success:
                return response_builder.success().ok_200().get_response()
            return (
                response_builder.fail()
                .not_found_404()
                .message("Not Found")
                .get_response()
            )
        except PermissionDenied:
            return (
                response_builder.fail()
                .user_forbidden_403()
                .message("Cannot delete other reviews")
                .get_response()
            )
        except Exception as e:
            print(f"ReviewUpdateDeleteView delete :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to update review"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )
