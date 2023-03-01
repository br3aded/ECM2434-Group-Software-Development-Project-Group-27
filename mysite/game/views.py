import secrets
import string

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Game , Group
from user.models import AppUser
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create lobby page
@login_required(login_url='/login/')
def create_lobby(request):
    return render(request,"game/createlobby.html")

# Create lobby request
@login_required(login_url='/login/')
def add_lobby(request):
    #gets submitted posts from create lobby page
    #may change when database implemented
    name = request.POST['lobby name']

    while True:
        game_code = ''.join(secrets.choice(string.ascii_uppercase) for i in range(5))

    # check if a game with this code already exists
        if not Game.objects.filter(game_code=game_code).exists():
            break
    app_user = get_object_or_404(AppUser, base_user=request.user)
    new_group = Group()
    new_group.group_leader = app_user
    new_group.save()

    player = request.POST['num of players'] # to be added
    rounds = request.POST['num of rounds'] # to be added
    
    game = Game(game_name = name,
                game_code = game_code,
                start_datetime = datetime.now(),
                game_state = 0,
                keeper_id = app_user,
                hosting_group = new_group,
                )
    game.save()
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view'))

def check_code(request):
    code = request.GET.get('code')
    game = Game.objects.filter(game_code=code).first()
    if game:
        return JsonResponse({'exists': True})
    else:
        return JsonResponse({'exists': False})

#generic lobby page
#this will change when lobby implemented

@login_required(login_url='/login/')
def join_lobby(request,game_code):
     game = Game.objects.filter(game_code=game_code).first()
     hosting_group = game.hosting_group
     if request.user in AppUser.objects.filter(group_members__hosting_group=game.hosting_group): 
        return HttpResponseRedirect(reverse('game:game'))
     else:
        hosting_group.group_members.add(get_object_or_404(AppUser, base_user=request.user))
        #there is a bug on this line above
        return HttpResponseRedirect(reverse('game:lobby_view'))


@login_required(login_url='/login/')
def lobby_view(request, game_code):
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

    return render(request,"game/gamelobby.html", {"username": request.user.username, "gamecode": game_code})

def set_task_view(request):
    return render(request,"game/setting-task.html", {"username": request.user.username})

'''
def set_task():
    code for setting task here

def response_task():
    code for responding to task here

def rank_tasks():
    code for ranking tasks here

'''

# /game url
@login_required(login_url='/login/')
def members(request):
    return render(request,"game/join_lobby.html", {"username": request.user.username})


@login_required(login_url='/login/')    
def get_lobby_code(request):
    if request.method == "POST":
        code = request.POST["enter-code"]
        return code

def test_get_variable(request):
    output = "pupper"
    return HttpResponse(request.POST[output])

def player_lobbys(request):
    member = get_object_or_404(AppUser, base_user=request.user)
    hosting_groups = Group.objects.filter(group_members=member)
    games = Game.objects.filter(hosting_group__in=hosting_groups)
    return render(request,"game/player_lobbys.html", {'lobby_list' : games})
