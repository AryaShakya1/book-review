from django.urls import path

from app.views.book import BookView
from app.views.user import login

urlpatterns = [
    path("v1/books/", BookView.as_view(), name="book"),
    path("v1/user/login/", login, name="login"),
]
