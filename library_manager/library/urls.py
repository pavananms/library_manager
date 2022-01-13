"""library_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/books', views.books, name='books'),
    path('api/v0/library_books', views.library_books, name='library_books'),
    path('api/v0/library_activities/check_out', views.library_activities_check_out, name='library_activities_check_out'),
    path('api/v0/library_activities/check_in', views.library_activities_check_in, name='library_activities_check_in'),
    path('api/v0/library_activities/list_books_for_user/<int:id>',
         views.library_activities_list_for_user,
         name='library_activities_list_for_user'),

]
