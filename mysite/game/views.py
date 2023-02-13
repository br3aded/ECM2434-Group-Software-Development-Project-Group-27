from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def create_lobby(request):
    return render(request,"game/createlobby.html")

def add_lobby(request):
    #gets submitted posts from create lobby page
    #may change when database implemented
    name = request.POST['lobby name']
    code = request.POST['lobby code']
    player = request.POST['num of players']
    rounds = request.POST['num of rounds']
    #add code here for creating a new lobby item in database when implemented
    #should add tests once completed
    return HttpResponseRedirect(reverse('game:lobby_view'))

#generic lobby page
#this will change when lobby implemented
def lobby_view(request):
    return render(request,"game/lobby.html")