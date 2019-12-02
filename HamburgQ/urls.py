from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Game.urls')),
    path('', include('social_django.urls', namespace='social')),
]