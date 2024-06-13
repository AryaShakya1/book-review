from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from app.builders.response_builder import ResponseBuilder


@api_view(["POST"])
def login(request):
    response_builder = ResponseBuilder()
    try:
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response_object = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return (
                response_builder.result_object(response_object)
                .success()
                .ok_200()
                .get_response()
            )
        else:
            return (
                response_builder.result_object({"message": "Invalid credentials"})
                .fail()
                .bad_request_400()
                .message("Bad Request")
                .get_response()
            )
    except Exception as e:
        print(f"User login :: exception:: {e}")
        return (
            response_builder.result_object({"message": "Unable to login user"})
            .fail()
            .internal_error_500()
            .message("Internal Error")
            .get_response()
        )

