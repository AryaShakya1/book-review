from django.urls import path
from app.views.book import (
    BookDetailView,
    BookSearchView,
    BookUpdateDeleteView,
    BookView,
)
from app.views.review import BookReviewView, ReviewUpdateDeleteView, ReviewView
from app.views.user import login, register

urlpatterns = [
    # books
    path("v1/books/", BookView.as_view(), name="book"),
    path("v1/books/search/", BookSearchView.as_view(), name="book"),
    path("v1/books/details/", BookDetailView.as_view(), name="book-detail"),
    path(
        "v1/books/<uuid:book_id>/",
        BookUpdateDeleteView.as_view(),
        name="book-update-delete",
    ),
    # reviews
    path("v1/reviews/", ReviewView.as_view(), name="review"),
    path(
        "v1/reviews/<uuid:review_id>/",
        ReviewUpdateDeleteView.as_view(),
        name="review-update-delete",
    ),
    path(
        "v1/books/<uuid:book_id>/reviews/",
        BookReviewView.as_view(),
        name="book-reviews-get",
    ),
    # user
    path("v1/user/login/", login, name="login"),
    path("v1/user/register/", register, name="register"),
]
