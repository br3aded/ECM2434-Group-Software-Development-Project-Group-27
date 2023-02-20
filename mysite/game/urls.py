from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('add_lobby',views.add_lobby ,name='add_lobby'),
    path('lobby',views.lobby_view,name='lobby_view'), #should include game code in lobby name
    path('join_lobby',views.lobby_view,name='join_lobby'),
    path('game/', views.members, name='game'),
]
