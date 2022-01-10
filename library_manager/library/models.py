from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Libraries(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    isbn_num = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField()

class LibraryActivities(models.Model):
    activities = [
        ('check_in', 'check_in'),
        ('check_out', 'check_out'),
        ]
    library_activity_id = models.AutoField(primary_key=True)
    activity_type = models.CharField(max_length=200, choices = activities)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    library_book_id = models.ForeignKey('LibraryBooks', on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField()
    checked_in_at = models.DateTimeField()
    
class LibraryBooks(models.Model):
    library_book_id = models.AutoField(primary_key=True)
    library_id = models.ForeignKey(Libraries, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    last_library_activity_id = models.ForeignKey(LibraryActivities, on_delete=models.CASCADE, null=True)
    
