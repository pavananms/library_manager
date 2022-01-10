import pdb
from django.shortcuts import render
from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Books, LibraryBooks
from .serializers import BooksSerializer, LibraryBooksSerializer

def books(request):
    if request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BooksSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(book_serializer.data, status = status.HTTP_400_BAD_REQUEST)

def library_books(request):
    if request.method == 'POST':
        library_books_data = JSONParser().parse(request)
        library_books_serializer = LibraryBooksSerializer(data=library_books_data)
        if library_books_serializer.is_valid():
            library_books_serializer.save()
            return JsonResponse(library_books_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(library_books_serializer.data, status = status.HTTP_400_BAD_REQUEST)





