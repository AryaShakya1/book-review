from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.builders.response_builder import ResponseBuilder
from app.services.book_service import BookService
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.core.exceptions import PermissionDenied


class BookView(APIView):

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
            book_service = BookService()
            books = book_service.get_all_books()
            return (
                response_builder.result_object(books).success().ok_200().get_response()
            )
        except Exception as e:
            print(f"BookView get :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to get books"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )

    def post(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            book_service = BookService()
            book_data = request.data.copy()
            book_data["created_by"] = request.user.id
            book, errors = book_service.create_book(book_data)
            if book:
                return (
                    response_builder.result_object(book)
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
            print(f"BookView post :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to create book"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )


class BookUpdateDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, book_id):
        response_builder = ResponseBuilder()
        try:
            book_service = BookService()
            book_data = request.data
            book, errors = book_service.update_book(book_id, book_data, request.user)
            if book:
                return (
                    response_builder.result_object(book)
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
                .message("Cannot edit other books")
                .get_response()
            )
        except Exception as e:
            print(f"BookUpdateDeleteView put :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to update book"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )

    def delete(self, request, book_id):
        response_builder = ResponseBuilder()
        try:
            book_service = BookService()
            success = book_service.delete_book(book_id, request.user)
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
                .message("Cannot delete other books")
                .get_response()
            )
        except Exception as e:
            print(f"BookUpdateDeleteView delete :: exception:: {e}")
            return (
                response_builder.result_object({"message": "Unable to update book"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )
