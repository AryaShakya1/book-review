from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.builders.response_builder import ResponseBuilder
from app.services.book_service import BookService
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.core.exceptions import PermissionDenied


class HealthView(APIView):

    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            return (
                response_builder.result_object({"message": "Health Check Passed"})
                .success()
                .ok_200()
                .get_response()
            )
        except Exception as e:
            print(f"HealthView get :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Health Check Failed"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )
