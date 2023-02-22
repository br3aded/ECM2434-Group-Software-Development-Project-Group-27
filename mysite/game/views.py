from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from .models import Game 
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required



LOGGED_IN = True

@login_required(login_url='/login/')
def create_lobby(request):
    return render(request,"game/createlobby.html")

@login_required(login_url='/login/')
def add_lobby(request):
    #gets submitted posts from create lobby page
    #may change when database implemented
    name = request.POST['lobby name']
    code = request.POST['lobby code']
    player = request.POST['num of players']
    rounds = request.POST['num of rounds']
    game_master = request.user
    game = Game(start_datetime = datetime.now(),end_date = '', max_points = '', hosting_group = '') #will change when database is added
    game.save()
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view'))

#generic lobby page
#this will change when lobby implemented
@login_required(login_url='/login/')
def lobby_view(request):
    return render(request,"game/gamelobby.html")

'''
def members(request):
    template = loader.get_template('join_lobby.html')
    return render(request,"game/gamelobby.html")
'''

# /game url
@login_required(login_url='/login/')
def members(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    template = loader.get_template('game/join_lobby.html')
    return HttpResponse(template.render())

    
def get_lobby_code(request):
    if request.method == "POST":
        code = request.POST["enter-code"]
        return code
