from django.urls import path

from .views import index_view

app_name = 'index_page'

urlpatterns = [
    path('', index_view)
]