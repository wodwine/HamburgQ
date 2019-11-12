from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Quiz,Question,WaitingRoom,Player,Choice
from django.contrib.auth import logout
from random import randint
from django.urls import reverse
from django.views import generic
import sqlite3


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
    try:
        quiz_name = request.POST['quiz_name']
    except:
        return redirect(reverse("Game:login_host"))
    get_type = Quiz.objects.filter(quizz_name = quiz_name)[0]
    get_time = request.POST['time']
    try:
        room_unique_id = get_random_id()
        waiting_room = WaitingRoom(room_name = get_name,room_id = room_unique_id,quiz_type = get_type,time = get_time)
        waiting_room.save()
        host = Player(player_name=str(request.user.username),room = waiting_room)
        host.save() 

    except:
        return redirect(reverse("Game:login_host"))
    else:
        return redirect(reverse("Game:WR_host",args=[str(waiting_room.room_id)]))

def login_guest(request):
    return render(request,'Login/loginguest.html')

def redirdirect_guest(request):
    get_code = request.POST['roomCode']
    get_name = request.POST['playerName']
    return redirect

def waiting_room_host(request,RoomId):
    waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
    all_player = waiting_room.player_set.all()
    context = {'room' : waiting_room,'all_player':all_player}
    return render(request,'WaitingRoom/WRhost.html',context)

def waiting_room_guest(request,RoomId):
    if request.method == "POST":
        get_name = request.POST['player_name']
        waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
        player_list = waiting_room.player_set.all()
        if get_name not in player_list:
            player = Player(player_name=str(get_name),room = waiting_room)
            player.save()
        else:
            return redirect(reverse("Game:login_guest"))
        all_player = waiting_room.player_set.all()
        context = {'room' : waiting_room,'all_player' : all_player,'current_player':player}
        return render(request,'WaitingRoom/WRguest.html',context)
    else:
        return redirect(reverse('Game:login_guest'))

def submit_answer(request):
    if request.method != "POST":
        return redirect(reverse('Game:start_quiz'))
    answer = request.POST["radio_answer"]
    answer = answer.split("$$")
    player = Player.objects.filter(id = answer[0])[0]
    if Choice.objects.filter(id = answer[1])[0].answer == 'True':
        player.add_score()
    player.progress()
    return redirect(reverse('Game:start_quiz' ,args=[answer[2],player.player_name] ))

def get_player_next_question(player):
    waiting_room = player.room
    return Quiz.objects.filter(id = waiting_room.quiz_type_id)[0].question_set.all()[player.current_question]
    
def start_quiz(request,RoomId,PlayerName):
    waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
    quiz = get_object_or_404(Quiz, id=waiting_room.quiz_type_id)
    questions = Question.objects.filter(quizz_id_id=waiting_room.quiz_type_id)
    choices_list=[]
    player = Player.objects.get(player_name=PlayerName,room=waiting_room)
    question = get_player_next_question(player)
    choices_list = question.choice_set.all()
    context = {'room' : waiting_room , 'quiz':quiz ,'questions':questions ,'choices':choices_list,'current_player':player,'number':len(questions)}
    return render(request, 'Game/play.html', context)

def log_out(request):
    logout(request)
    return redirect('Game:home')

def log_out_host(request,roomid):
    instance_room = WaitingRoom.objects.get(room_id=roomid)
    instance_room.delete()
    return redirect(reverse('Game:login_host'))

def log_out_guest(request,player_id):
    instance = Player.objects.get(id=player_id)
    instance.delete()
    return redirect(reverse('Game:login_guest'))