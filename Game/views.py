from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Quiz,Question,WaitingRoom,Player
from django.contrib.auth import logout
from random import randint
from django.urls import reverse
from django.views import generic


def get_random_id():
    new_name = ""
    for times in range(6):
        new_name += str(randint(1,9))
    new_name = int(new_name)
    query = WaitingRoom.objects.filter(room_id = new_name)
    if len(query) == 0:
        return new_name
    else:
        get_random_id()


def admin(request):
    return HttpResponse('admin')

def home(request):
    return render(request,'Home/mainpage.html')

def log_out(request):
    logout(request)
    return redirect('Game:home')

def how_to_play(request):
    return render(request,'Home/htp.html')

def contact_us(request):
    return render(request,'Home/contact.html')

def login(request):
    return render(request,'Login/login.html')

def login_host(request):
    quiz = Quiz.objects.all()
    context = {'quiz':quiz}
    return render(request,'Login/loginhost.html',context)

def create_room(request):
    get_name = request.POST['roomName']
    get_type = Quiz.objects.filter(quizz_name = request.POST['quiz_name'])[0]
    get_time = request.POST['time']
    try:
        room_unique_id = get_random_id()
        waiting_room = WaitingRoom(room_name = get_name,room_id = room_unique_id,quiz_type = get_type,time = get_time)
        host = Player(player_name=str(request.user.username),room_id_player = room_unique_id)
        host.save()
        waiting_room.save()
        return redirect(reverse('Game:WR_host'))
    except:
        ##return error
        return redirect(reverse("Game:WR_host",args=[str(waiting_room.room_id)]))

def login_guest(request):
    return render(request,'Login/loginguest.html')

def redirdirect_guest(request):
    get_code = request.POST['roomCode']
    get_name = request.POST['playerName']
    return redirect

def waiting_room_host(request,RoomId):
    waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
    all_player = Player.objects.filter(room_id_player = RoomId)
    context = {'room' : waiting_room,'all_player':all_player, 'round':1}
    return render(request,'WaitingRoom/WRhost.html',context)

def waiting_room_guest(request,RoomId):
    if request.method == "POST":
        get_name = request.POST['player_name']
        waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
        player_list = []
        for i in Player.objects.filter(room_id_player = RoomId):
            player_list.append(i.player_name)
        if get_name not in player_list:
            player= Player(player_name=str(get_name),room_id_player = RoomId)
            player.save()
        all_player = Player.objects.filter(room_id_player = RoomId)
        context = {'room' : waiting_room,'all_player' : all_player,'current_player':get_name}
        return render(request,'WaitingRoom/WRguest.html',context)
    else:
        return redirect(reverse('Game:login_guest'))

def start_quiz(request,RoomId):
    context = {'RoomId':RoomId}
    return render(request, 'Game/play.html', context)
