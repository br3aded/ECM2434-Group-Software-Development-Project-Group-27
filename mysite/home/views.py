from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from user.models import AppUser

#This is the landing page for the website
def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

#this loads the page used for logging in
def login_view(request):
    return render(request,"login.html")

#called from login.html this takes the details entered onto the page and creates a new user object
def add_user(request):
  #This makes sure usernames are unique
  if User.objects.filter(username = request.POST['Username']).first():
        messages.error(request, "This username is already taken")
        return HttpResponseRedirect(reverse('home:login'))
  user = User.objects.create_user(username = request.POST['Username'],
  email = request.POST['Email'],
  password = request.POST['Password']
  )
  new_user = AppUser(base_user = user,
                     points = 0)
  new_user.save()
  return HttpResponseRedirect(reverse('home:login'))

#Uses djangos authentication system to log in a user , called from login.html
def login_user(request):
  user = authenticate(request, username=request.POST['Username'], password=request.POST['Password'])
  if user is not None:
      login(request,user)
      return HttpResponseRedirect(reverse('game:game'), {'username': request.user.username})
  else:
      # Return an 'invalid login' error message.
      return HttpResponseRedirect(reverse('home:login'))

# Uses djangos authentication system to log out a user , this is used by the sidebar on most pages
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:home'))

  
