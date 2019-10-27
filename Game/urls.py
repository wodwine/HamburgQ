from django.urls import path
from . import views

app_name = 'Game'
urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('login/',views.login),
    path('login/host',views.login_host,name = "login_host"),
    path('login/guest',views.login_guest),
    path('test/', views.hi),
    path('play/<str:quiz_name>/<int:question_number>/',views.play_quiz,name = "play_quiz"),
]
