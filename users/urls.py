from django.urls import path
from .views import user_list, user_detail_page
urlpatterns = [
    path('users/', user_list),
    path('detail/', user_detail_page),
]