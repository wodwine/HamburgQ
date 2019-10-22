from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.hi),
    path('play/<str:quiz_name>/<int:question_number>/',views.play_quiz,name = "play_quiz"),
]
