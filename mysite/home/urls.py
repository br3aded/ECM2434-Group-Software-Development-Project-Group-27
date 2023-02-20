from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.members, name='home'),
    path('login/', views.login, name='login'),
]