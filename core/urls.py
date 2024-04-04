from django.contrib import admin
from django.urls import path, include
from .view import page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", page),
    path('', include("library.urls")),
    path("", include("users.urls")),
]
