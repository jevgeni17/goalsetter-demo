from django.urls import path
from django.urls import re_path
from .views import index

urlpatterns = [
    path('', index, name="index"),
]