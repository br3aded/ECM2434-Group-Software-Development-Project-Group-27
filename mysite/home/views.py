from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def login_view(request):
    return render(request,"login.html")

def add_user(request):
  if User.objects.filter(username = request.POST['Username']).first():
        messages.error(request, "This username is already taken")
        return HttpResponseRedirect(reverse('home:login'))
  User.objects.create_user(username = request.POST['Username'],
  email = request.POST['Email'],
  password = request.POST['Password']
  )
  return HttpResponseRedirect(reverse('home:login'))

def login_user(request):
  user = authenticate(request, username=request.POST['Username'], password=request.POST['Password'])
  if user is not None:
      login(request,user)
      return HttpResponseRedirect(reverse('home:home'), {'username': user})
  else:
      # Return an 'invalid login' error message.
      return HttpResponseRedirect(reverse('home:login'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:home'))

  