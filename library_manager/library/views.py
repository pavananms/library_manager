import datetime
import pdb

from django.shortcuts import render
from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets

from .models import Books, LibraryActivities, LibraryBooks, Users
from .serializers import \
    BooksSerializer, LibraryActivitiesCheckoutSerializer, LibraryActivitiesCheckinSerializer, LibraryBooksSerializer, LibraryActivitiesUsersSerializer, LibraryActivitiesLibrarySerializer

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

def library_activities_check_out(request):
    if request.method == 'POST':
        check_out_data = JSONParser().parse(request)
        check_out_serializer = LibraryActivitiesCheckoutSerializer(data = check_out_data)
        
        if check_out_serializer.is_valid():
            saved_activity = check_out_serializer.save()
            saved_activity.checked_out_at = datetime.datetime.now()
            saved_activity.save()
            return JsonResponse(check_out_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(check_out_serializer.data, status = status.HTTP_400_BAD_REQUEST)

def library_activities_check_in(request):
    if request.method == 'POST':
        check_in_data = JSONParser().parse(request)
        check_in_serializer = LibraryActivitiesCheckoutSerializer(data = check_in_data)
        if check_in_serializer.is_valid():
            saved_activity = check_in_serializer.save()
            saved_activity.checked_in_at = datetime.datetime.now()
            saved_activity.save()
            return JsonResponse(check_in_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(check_in_serializer.data, status = status.HTTP_400_BAD_REQUEST)

#TODO: Serializer strangely doesnt take queryset as a valid input. Fix this
def library_activities_list_for_user(request, id):
    if request.method == 'GET':
        # activities = LibraryActivities.objects.all()
        user_activities = LibraryActivities.objects.all().filter(user=id, checked_out_at != Null)

        user_activites_serializer = LibraryActivitiesUsersSerializer(data=user_activities)

        if user_activites_serializer.is_valid():
            return JsonResponse(user_activites_serializer.data, status = status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(user_activites_serializer.data, status = status.HTTP_400_BAD_REQUEST)

def library_activities_list_book(request, id):
    if request.method == 'GET':
        # activities = LibraryActivities.objects.all()
        library_activities = LibraryActivities.objects.all().filter(user=id, checked_out_at)

        library_activites_serializer = LibraryActivitiesLibrarySerializer(data=library_activites)

        if library_activites_serializer.is_valid():
            return JsonResponse(library_activites_serializer.data, status = status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(library_activites_serializer.data, status = status.HTTP_400_BAD_REQUEST)





