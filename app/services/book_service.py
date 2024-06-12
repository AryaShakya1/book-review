from app.models.book import Book
from app.serializers.book_serializer import BookSerializer
from django.core.exceptions import PermissionDenied


class BookService:

    def get_all_books(self):
        books = Book.get_all_books()
        return BookSerializer(books, many=True).data

    def get_book_by_id(self, id):
        book = Book.get_book_by_id(id=id)
        if not book:
            return None
        return BookSerializer(book).data

    def get_book_by_title(self, title):
        book = Book.get_book_by_title(title=title)
        if not book:
            return None
        return BookSerializer(book).data

    def create_book(self, book_data):
        serializer = BookSerializer(data=book_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    def update_book(self, book_id, data, user):
        book = Book.get_book_by_id(id=book_id)
        if not book:
            return None, "Book not Found"
        if book.created_by != user:
            raise PermissionDenied("You do not have permission to edit this book.")
        serializer = BookSerializer(book, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    def delete_book(self, book_id, user):
        book = Book.get_book_by_id(id=book_id)
        if not book:
            return None, "Book not Found"
        if book.created_by != user:
            raise PermissionDenied("You do not have permission to edit this book.")
        if not book:
            return False
        book.delete()
        return True
