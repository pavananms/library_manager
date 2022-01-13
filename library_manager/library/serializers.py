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

class LibraryActivitiesCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivities
        fields = ('activity_type',
                  'user_id',
                  'library_book_id')

class LibraryActivitiesCheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivities
        fields = ('activity_type',
                  'user_id',
                  'library_book_id')

class LibraryActivitiesUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivities
        fields = ['user']

class LibraryActivitiesBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivities
        fields = ['library']
