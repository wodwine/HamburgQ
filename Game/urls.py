from django.urls import path
from . import views
from django.conf.urls import handler404
from Game import views

app_name = 'Game'
urlpatterns = [
    path('',views.home),
    path('admin/',views.admin,name="admin"),
    path('home/',views.home,name="home"),
    path('logout/',views.log_out,name="log_out"),
    path('logouthost/<int:roomid>',views.log_out_host,name="log_out_host"),
    path('logoutguest/<int:player_id>',views.log_out_guest,name="log_out_guest"),
    path('login/',views.login,name = "login"),
    path('login/host/',views.login_host,name = "login_host"),
    path('create/',views.create_room,name = 'create_room'),
    path('login/guest/',views.login_guest,name = 'login_guest'),
    path('WRhost/<int:RoomId>/',views.waiting_room_host,name = 'WR_host'),
    path('WRguest/<int:RoomId>/',views.waiting_room_guest,name = 'WR_guest'),
    path('play/<int:RoomId>/<str:PlayerName>/',views.start_quiz, name = "start_quiz"),
    path('score/',views.submit_answer,name = "submit_answer"),
    path('wait_result/<int:RoomId>/<str:PlayerName>/',views.personal_result,name = 'result'),
    path('all_result/<int:RoomId>/<str:PlayerName>/',views.all_result,name = 'all_result'),
]

handler404 = views.error_404
handler500 = views.error_500