from django.urls import path
from .views import library_page, library_books_page
urlpatterns = [
    path('library/', library_page),
    path('books/', library_books_page),
]