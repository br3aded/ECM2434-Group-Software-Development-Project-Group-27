from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from .models import Game 
from django.contrib.auth.models import User
from datetime import datetime
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
    game = Game(start_datetime = datetime.now(),end_date = '', max_points = '', hosting_group = '') #will change when database is added
    game.save()
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view'))

#generic lobby page
#this will change when lobby implemented
@login_required(login_url='/login/')
def lobby_view(request,user_id,game_code):
    '''
    rough outline of what the lobby should look like

    lobby = get game_code lobby

    if lobby state == 1:
        return render waiting for players to join html
    if lobby state == 2:
        if user_id == lobby get game_master:
            return render set tasks html
        else:
            return render waiting for task html
    if lobby state == 3:
        if user_id == lobby get game_master:
            return render waiting for response html (possibly display active number of responses)
        else:
            return render response to task html
    if lobby state == 4:
        if user_id == lobby get game_master:
            return render for ranking tasks html
        else:
            return render waiting for ranking html
        return render template 4
    if lobby state == 5:
        return render results html (possibly add a button that will move state once all players have clicked it)
    if lobby state == 6:
        if lobby current round == total rounds:
            return render display final results (possibly add a button here to delete lobby once all players have clicked it)
        else:
            lobby current round += 1
            lobby current state = 2
            return render lobby view

    '''

    return render(request,"game/gamelobby.html")

'''
def set_task():
    code for setting task here

def response_task():
    code for responding to task here

def rank_tasks():
    code for ranking tasks here

'''




'''
def members(request):
    template = loader.get_template('join_lobby.html')
    return render(request,"game/gamelobby.html")
'''

# /game url
@login_required(login_url='/login/')
def members(request):
    template = loader.get_template('game/join_lobby.html')
    return HttpResponse(template.render())


@login_required(login_url='/login/')    
def get_lobby_code(request):
    if request.method == "POST":
        code = request.POST["enter-code"]
        return code