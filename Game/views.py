from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz,Question

def hi(request):
    return HttpResponse('hi')
    
def play_quiz(request, quiz_name, question_number):
    quiz = get_object_or_404(Quiz, quizz_name = quiz_name)
    q = {'question':quiz.question_set.all()[question_number-1]}
    return render(request,'Game/question_play.html',q)

def home(request):
    return render(request,'Home/mainpage.html')

def how_to_play(request):
    return render(request,'Home/htp.html')

def contact_us(request):
    return render(request,'Home/contact.html')

def login(request):
    return render(request,'Login/login.html')

def login_host(request):
    return render(request,'Login/loginhost.html')

def login_guest(request):
    return render(request,'Login/loginguest.html')

def waiting_room_host(request,room_id):
    context = {'id' : room_id}
    return render(request,'WaitingRoom/WRhost.html',context)

def waiting_room_guest(request,room_id):
    context = {'id' : room_id}
    return render(request,'WaitingRoom/WRguest.html',context)