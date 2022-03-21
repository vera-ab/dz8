from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
    path('', include('index_page.urls', namespace='index_page')),
    path('random/', include('my_random.urls', namespace='random')),
]
