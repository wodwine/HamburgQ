from django.urls import path
from . import views

app_name = 'Game'
urlpatterns = [
    path('',views.home),
    path('home/',views.home,name="home"),
    path('logout/',views.log_out,name="log_out"),
    path('howtoplay/',views.how_to_play),
    path('contact/',views.contact_us),
    path('login/',views.login,name = "login"),
    path('login/host/',views.login_host,name = "login_host"),
    path('create/<str:try_room_name>/',views.create_room,name = 'create_room'),
    path('login/guest',views.login_guest,name = 'login_guest'),
    path('WRhost/<str:room_id>',views.waiting_room_host,name = 'WR_host'),
    path('WRguest/<str:room_id>',views.waiting_room_guest,name = 'WR_guest'),
    path('test/', views.hi),
    path('play/<str:quiz_name>/<int:question_number>/',views.play_quiz,name = "play_quiz"),
]
