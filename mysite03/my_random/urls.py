from django.urls import path

from .views import random_view

app_name = 'random'

urlpatterns = [
    path('', random_view)
]