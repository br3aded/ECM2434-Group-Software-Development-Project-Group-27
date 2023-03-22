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

#@login_required prevents users from accessing page without having logged in and will redirected to login page if they are not

# Loads the createlobby.html page
@login_required(login_url='/login/')
def create_lobby(request):
    return render(request,"game/createlobby.html")

# Adds a new game object to the databsae
@login_required(login_url='/login/')
def add_lobby(request):
    #gets submitted posts from create lobby page
    name = request.POST['lobby name']
    player = request.POST['num of players'] 
    rounds = request.POST['num of rounds']
    #generates a random 5 letter game code
    while True:
        game_code = ''.join(secrets.choice(string.ascii_uppercase) for i in range(5))
        #checks the game code is unique
        if not Game.objects.filter(game_code=game_code).exists():
            break
    #gets the currently logged in user
    app_user = get_object_or_404(AppUser, base_user=request.user)
    #creates a new group object
    new_group = Group(group_leader = app_user,
                      max_players = player,)
    new_group.save()
    #creates a new game object
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
    #sends the user to the lobby_view page
    return HttpResponseRedirect(reverse('game:lobby_view', kwargs={'game_code' : game_code}))

#this adds a user to a game when they enter a correct code into the text box
@login_required(login_url='/login/')
def add_user(request):
    #gets game code , gets game object associated with code and gets currently logged in app user
    game_code = (request.GET.get('code')).upper()
    game = Game.objects.get(game_code=game_code)
    app_user = get_object_or_404(AppUser, base_user=request.user)
    #conditions for joining a lobby
    if game and (game.hosting_group.group_members.all()).count() < game.hosting_group.max_players and game.game_state == 0 and game.hosting_group.group_leader != app_user:
        game.hosting_group.group_members.add(app_user)
        #returns true if game exists and user is added
        return JsonResponse({'exists': True})
    else:
        #returns false if conditions not met
        return JsonResponse({'exists': False})

#This is the main code for the game systems
@login_required(login_url='/login/')
def lobby_view(request, game_code):
    #gets game with passed game code and currently logged in user
    game = Game.objects.get(game_code=game_code)
    app_user = get_object_or_404(AppUser, base_user=request.user)
    print(app_user)
    #loads correct pages for game state 0 based on is the user is a host or not
    if game.game_state == 0:
        if game.hosting_group.group_leader == app_user:
            return render(request,"game/gamelobby-client.html", {"game_code" : game_code})
        else:
            return render(request,"game/gamelobby-client no start.html", {"game_code" : game_code}) # change to other page for 

    if game.game_state == 1:
        #checks to see if a task has been set , if true game state is iterated
        print(game.current_round_name)
        if game.current_round_name != "":
            game.game_state = 2
            game.save()
            return HttpResponseRedirect(reverse('game:lobby_view', kwargs={'game_code' : game_code}))
        else:
            if app_user == game.hosting_group.group_leader:
                return HttpResponseRedirect(reverse('game:setting_task_view', kwargs={'game_code' : game_code}))
            else:
                return render(request,"game/waiting_for_task.html", kwargs={"game_code" : game_code})

    if game.game_state == 2:
        #checks if all the players have submitted response to tasks
        if (game.submissions.all()).count() == game.hosting_group.max_players:
            game.game_state = 3
            game.save()
            return HttpResponseRedirect(reverse('game:lobby_view', kwargs={'game_code' : game_code}))
        else:
            #if game host render waiting screen
            if app_user == game.hosting_group.group_leader:
                return render(request,"game/waiting_response.html", {"game_code" : game_code})
            else:
                submisssions = app_user.submission_set.all()
                if submisssions.exists():
                    return render(request,"game/waiting_response.html", {"game_code" : game_code})
                else:
                    #else redirect to view for submiting tasks
                    return HttpResponseRedirect(reverse('game:submit_task', {'game_code' : game_code}))
    #loads correct pages for game state 3 based on if the user is host or not

    if game.game_state == 3:
        if app_user == game.hosting_group.group_leader:
            #redirects to ranking view for game master
            return HttpResponseRedirect(reverse('game:ranking_view', {'game_code' : game_code}))
        else:
            #renders waiting page for players
            return render(request,"game/waiting_for_ranking.html", {"game_code" : game_code})
    #loads correct pages for game state 4 based on if the user is host or not
    if game.game_state == 4:
        #checks to see if all players have viewed results when the player clicks the ready up button on the page there previous submission is deleted
        if game.submission == None:
            game.game_state = 5
            game.save()
            return HttpResponseRedirect(reverse('game:lobby_view', kwargs={'game_code' : game_code}))
        else:
            #returns results screen
            return render(request,"game/ranking.html", {"game_code" : game_code})
    #loads correct pages for game state 5 based on if the user is host or not
    if game.game_state == 5:
        #if the round is the final round load end of game results page
        if game.current_round_number == game.max_rounds:
            return render(request,"game/results.html", {"game_code" : game_code})
            #change html to results page
        else:
            #starts a new round
            game.current_round_number += 1
            game.game_state = 2
            game.current_round_name = ""
            game.save()
            return HttpResponseRedirect(reverse('game:lobby_view', {'game_code' : game_code}))

#view used to render set task page
@login_required(login_url='/login/')
def set_task_view(request, game_code):
    #gets three random tasks from task.txt and passed in the render
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

#used to set a new task in game
@login_required(login_url='/login/')
def set_task(request, game_code):
    #gets the posts from the form in setting-task.html
    if request.method == 'POST':
        dropdown = request.POST["eco-tasks"]
        input_box = request.POST["Task desc"]
        #if input box is empty used dropdown box
        if input_box == None:
            task_name = dropdown
        #if input box isnt empty used input box text
        else:
            task_name = input_box
        #adds task to assocaited game model
        game = Game.objects.get(game_code=game_code)
        game.current_round_name = task_name
        game.save()
    return HttpResponseRedirect(reverse('game:lobby_view' , kwargs={'game_code' : game_code}))

#default lobby
@login_required(login_url='/login/')
def members(request):
    return render(request,"game/join_lobby.html", {"username": request.user.username})

#used to show all the games the user is a part of 
@login_required(login_url='/login/')
def player_lobbys(request):
    #gets all the game objects the user is a member of
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
    #renders player_lobbys page with a list of associated game objects
    return render(request,"game/player_lobbys.html", {'lobby_list' : games})

#pass the game code to here
def submit_task(request, game_code):
    if request.method == "POST":
        game = Game.objects.filter(game_code=game_code).first()
        user = get_object_or_404(AppUser, base_user=request.user)
        submission = Submission(game_id = game,
                                user_id = user,
                                submission = request.FILES['submission'])
        submission.save()
        return HttpResponseRedirect('../lobby/' + game_code)
    else:
        return render(request, 'game/submit_task.html', {'game_code' : game_code})

#renders the page used to take pictures
@login_required(login_url='/login/')
def take_picture(request,game_code):
    return render(request, 'game/take_picture.html', {'game_code' : game_code})


def test(request):
    return render(request, 'game/test.html')

#renders page used in final rankings
@login_required(login_url='/login/')
def end_game(request):
    return render(request, 'game/end-of-game.html')

def inc_gamestate(request):
    game_code = (request.GET.get('code')).upper().replace(" ", "")
    print(game_code)
    game = Game.objects.get(game_code=game_code)
    game.game_state = 1
    game.save()
    print(game.game_state)
    return JsonResponse({'exists': True})

