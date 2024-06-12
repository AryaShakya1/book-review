from django.urls import path

from app.views.book import BookUpdateDeleteView, BookView
from app.views.review import ReviewView
from app.views.user import login

urlpatterns = [
    path("v1/books/", BookView.as_view(), name="book"),
    path('v1/books/<uuid:book_id>/', BookUpdateDeleteView.as_view(), name='book-update-delete'),
    path("v1/reviews/", ReviewView.as_view(), name="review"),
    path("v1/user/login/", login, name="login"),
]
