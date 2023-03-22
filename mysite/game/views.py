import secrets
import string
import random

from django.db.models import BooleanField, Case, When
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Game , Group , Submission
from . import forms
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
    player = request.POST['num of players'] 
    rounds = request.POST['num of rounds']
    app_user = get_object_or_404(AppUser, base_user=request.user)
    new_group = Group(group_leader = app_user,
                      max_players = player,)
    new_group.save()
  
    game = Game(game_name = name,
                game_code = game_code,
                start_datetime = datetime.now(),
                game_state = 0,
                max_rounds = rounds,
                current_round_number = 1,
                current_round_name = "",
                hosting_group = new_group,
                )
    game.save()
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view', kwargs={'game_code' : game_code}))

#this need to be changed to reflect database changes
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

#pass the game code to here
@login_required(login_url='/login/')
def lobby_view(request, game_code):
    '''
    rough outline of what the lobby should look like

    game = Game.objects.filter(game_code=code).all()

    if game.game_state == 0:
        # add a condition here that will change the state to 1 if condition met
        return render(request,"game/waiting_for_players.html", {"game_code" : game_code})
    if lobby state == 1:
        if user_id == game get group_leader:
            return HttpResponseRedirect(reverse('game:setting_task_view', {'game_code' : game_code}))
        else:
            return render(request,"game/waiting_for_task.html", {"game_code" : game_code})
    if lobby state == 2:
        #need a condition for if submisions == max_players change to state 3
        if user_id == game get group_leader:
            return render(request,"game/waiting_for_response", {"game_code" : game_code})
        else:
            if user_id not in submission:
                return HttpResponseRedirect(reverse('game:response_task_view', {'game_code' : game_code}))
            else:
                return render(request,"game/waiting_for_response", {"game_code" : game_code})
    if lobby state == 3:
        if user_id == game get group_leader:
            return HttpResponseRedirect(reverse('game:rank_view', {'game_code' : game_code}))
        else:
            return render(request,"game/waiting_for_ranking", {"game_code" : game_code})
    if lobby state == 4:
        return render(request,"game/results.html", {"game_code" : game_code})
        #need a condition here for when moving onto state 5
    if lobby state == 5:
        if lobby current round == total rounds:
            return render display final results (possibly add a button here to delete lobby once all players have clicked it)
        else:
            lobby current round += 1
            lobby current state = 2
            return HttpResponseRedirect(reverse('game:lobby_view', {'game_code' : game_code}))

    '''
    return render(request,"game/gamelobby-client.html", {"username": request.user.username, "game_code": game_code})

#pass the game code to here
def set_task_view(request, game_code):
    f = open("game/static/tasks.txt","r")
    tasks = []
    randomTask = []
    for line in f:
        tasks.append(line)
    randomTaskNum = random.sample(range(len(tasks)),3)
    for num in randomTaskNum:
        randomTask.append(tasks[num])
    f.close()
    return render(request,"game/setting-task.html", {"username": request.user.username,"tasks": randomTask , "game_code" : game_code})

#pass the gamecode to here
def set_task(request, game_code):
    #code for setting task here
    if request.method == 'POST':
        dropdown = request.POST["eco-tasks"]
        input_box = request.POST["Task desc"]
        if input_box == None:
            task_name = dropdown
        else:
            task_name = input_box
        game = Game.objects.get(game_code=game_code)
        game.current_round_name = task_name
        game.save()
    return HttpResponseRedirect(reverse('game:lobby_view' , kwargs={'game_code' : game_code}))

#pass the game code to here
def response_task_view(request, game_code):
    return render(request,"game/respond-task.html", {"username": request.user.username})

#pass the game code to here
def response_task(request , game_code):
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
    groups = Group.objects.annotate(
        is_member=Case(
            When(group_leader=app_user, then=True),
            When(group_members=app_user, then=True),
            default=False,
            output_field=BooleanField(),
        )
    ).filter(is_member=True)

    games = Game.objects.filter(hosting_group__in=groups)
    return render(request,"game/player_lobbys.html", {'lobby_list' : games})

#pass the game code to here
def submit_task(request):
    if request.method == "POST":
        form = forms.createSubmission(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('./test')
    else:
        form = forms.createSubmission()
    return render(request, 'game/submit_task.html', { 'form': form })

#pass the game code to here
def take_picture(request,game_code):
    return render(request, 'game/take_picture.html', {'game_code' : game_code})


def test(request):
    return render(request, 'game/test.html')

def end_game(request):
    return render(request, 'game/end-of-game.html')

