from django.urls import path

from .views import my_whoami, source_code

app_name = 'about'

urlpatterns = [
    path('', my_whoami),
    path('whoami/', my_whoami),
    path('source_code/', source_code)
]
