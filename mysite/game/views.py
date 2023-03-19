import secrets
import string
import random

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
    player = request.POST['num of players'] 
    rounds = request.POST['num of rounds']
    
    game = Game(game_name = name,
                game_code = game_code,
                start_datetime = datetime.now(),
                game_state = 0,
                max_rounds = rounds,
                max_players = player,
                active_task_number = 0,
                #keeper_id = app_user,
                hosting_group = new_group,
                )
    game.save()
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view'))

def get_game_data(request):
    code = request.GET.get('code')
    game = Game.objects.filter(game_code=code).all()
    group = Group.objects.get(id=data["hosting_group_id"])
    if game and len(group) < game.max_players+1:
        data = (game.values()[0])
        app_user = get_object_or_404(AppUser, base_user=request.user)
        group.group_members.add(app_user)

        users = []

        for user in group.group_members.all():
            users.append(user.base_user.username)

        print(users)

        return JsonResponse({'exists': True, 'data': data, 'users': users})
    else:
        return JsonResponse({'exists': False})

@login_required(login_url='/login/')
def lobby_view(request,user_id=0, game_code=0):
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

    return render(request,"game/gamelobby-client.html", {"username": request.user.username, "gamecode": game_code})

def set_task_view(request):
    f = open("game/static/tasks.txt","r")
    tasks = []
    randomTask = []
    for line in f:
        tasks.append(line)
    randomTaskNum = random.sample(range(len(tasks)),3)
    for num in randomTaskNum:
        randomTask.append(tasks[num])
    f.close()
    return render(request,"game/setting-task.html", {"username": request.user.username,"tasks": randomTask})


def set_task(request):
    #code for setting task here
    if request.method == 'POST':
        dropdown = request.POST["eco-tasks"]
        input_box = request.POST["task-desc"]
        task_final = ""
        if input_box == "":
            task_final = dropdown
        else:
            task_final = input_box
        task = task_final
        task.save()
    return HttpResponseRedirect(reverse('game:lobby_view'))


def response_task_view(request):
    return render(request,"game/respond-task.html", {"username": request.user.username})

def response_task():
    #code for responding to task here
    
    return HttpResponseRedirect(reverse('game:lobby_view'))

'''
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
    app_user = get_object_or_404(AppUser, base_user=request.user)
    hosting_groups = Group.objects.filter(group_members=app_user)
    games = Game.objects.filter(hosting_group__in=hosting_groups)
    return render(request,"game/player_lobbys.html", {'lobby_list' : games})

def submit_task(request):
    return render(request, 'game/submit_task.html')

def take_picture(request):
    return render(request, 'game/take_picture.html')

def test(request):
    return render(request, 'game/test.html')
