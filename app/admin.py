from django.contrib import admin
from app.models.book import Book
from app.models.review import Review


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("idx", "title", "author", "publication_date")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("idx", "content", "user", "book")
