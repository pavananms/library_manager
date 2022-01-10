from rest_framework import serializers

from .models import Books, LibraryBooks, LibraryActivities

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('book_id',
                  'title',
                  'author_name',
                  'isbn_num',
                  'genre',
                  'description')

class LibraryBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBooks
        fields = ('library_id',
                  'book_id')
