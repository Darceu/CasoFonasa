from django.contrib import admin
from django.urls import path, include
from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('fonasa/home/', include('app.urls')),
    path('', home, name='default'),
    
]
