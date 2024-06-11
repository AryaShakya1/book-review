from app.models.book import Book
from app.serializers.book_serializer import BookSerializer


class BookService:

    def get_all_books(self):
        books = Book.get_all_books()
        return BookSerializer(books, many=True).data

    def get_book_by_id(self, id):
        book = Book.get_book_by_id(id=id)
        if not book:
            return None
        return BookSerializer(book).data

    def get_book_by_id(self, title):
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