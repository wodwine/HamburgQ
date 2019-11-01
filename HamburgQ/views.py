from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

def redirect_games(request):
    return redirect('/play/')
