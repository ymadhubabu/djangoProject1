from django.urls import path
from .views import json_view

urlpatterns = [
    path("", json_view, name="home"),
]