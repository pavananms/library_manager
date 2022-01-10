from django.contrib import admin
from .models import Libraries, LibraryBooks, Users, Books, LibraryActivities
# Register your models here.

admin.site.register(Libraries)
admin.site.register(Users)
admin.site.register(Books)
admin.site.register(LibraryActivities)
admin.site.register(LibraryBooks)
