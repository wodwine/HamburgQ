from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Quiz,Question,WaitingRoom
from django.contrib.auth import logout
from random import randint
from django.urls import reverse
from django.views import generic


# class IndexView(generic.ListView):
#     template_name = 'Login/loginhost.html'
#     context_object_name = 'latest_quiz_list'

#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Quiz.quizz_name

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


def hi(request):
    return HttpResponse('hi')
    
def play_quiz(request, quiz_name, question_number):
    quiz = get_object_or_404(Quiz, quizz_name = quiz_name)
    q = {'question':quiz.question_set.all()[question_number-1]}
    return render(request,'Game/question_play.html',q)

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

def page_objects(request):
  if request.method == 'POST':
    form = YourForm(request.POST)

    if form.is_valid():
      answer = form.cleaned_data['value']
      print(answer)

def create_room(request):

    get_name = request.POST['roomName']
    get_type = Quiz.objects.filter(quizz_name = request.POST['quiz_name'])[0]
    get_time = request.POST['time']

    try:
        waiting_room = WaitingRoom(room_name = get_name,room_id = get_random_id(),quiz_type = get_type,time = get_time)
        waiting_room.save()
        return redirect(reverse('Game:WR_host'))
    except:
        ##return error
        return redirect(reverse("Game:WR_host",args=[str(waiting_room.room_id)]))
def login_guest(request):
    return render(request,'Login/loginguest.html')

def waiting_room_host(request,RoomId):
    waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
    context = {'room' : waiting_room}
    return render(request,'WaitingRoom/WRhost.html',context)

def waiting_room_guest(request,RoomId):
    if request.method == "POST":
        get_name = request.POST['player_name']
        waiting_room = get_object_or_404(WaitingRoom, room_id=RoomId)
        context = {'room' : waiting_room,'name' :get_name}
        return render(request,'WaitingRoom/WRguest.html',context)