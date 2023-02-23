from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from .models import Game 
from user.models import User
from datetime import datetime

LOGGED_IN = True

def create_lobby(request):
    return render(request,"game/createlobby.html")

def add_lobby(request):
    #gets submitted posts from create lobby page
    #may change when database implemented
    name = request.POST['lobby name']
    code = request.POST['lobby code']
    player = request.POST['num of players']
    rounds = request.POST['num of rounds']
    game = Game(start_datetime = datetime.now(),end_date = '', max_points = '', hosting_group = '') #will change when database is added
    game.save()
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view'))

#generic lobby page
#this will change when lobby implemented
def lobby_view(request):
    return render(request,"game/gamelobby.html", {"username": "greedo"})

'''
def members(request):
    template = loader.get_template('join_lobby.html')
    return render(request,"game/gamelobby.html")
'''

# /game url
def members(request):
    template = loader.get_template('game/join_lobby.html')
    return HttpResponse(template.render())

    
def get_lobby_code(request):
    if request.method == "POST":
        code = request.POST["enter-code"]
        return code

def test_get_variable(request):
    output = "pupper"
    return HttpResponse(request.POST[output])
