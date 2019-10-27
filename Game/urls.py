from django.urls import path
from . import views

app_name = 'Game'
urlpatterns = [
    path('test/', views.hi),
    path('play/<str:quiz_name>/<int:question_number>/',views.play_quiz,name = "play_quiz"),
]
