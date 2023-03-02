from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('add_lobby',views.add_lobby ,name='add_lobby'),
    path('check_code', views.check_code, name='check_code'),
    path('lobby/<str:game_code>/',views.lobby_view,name='lobby_view'), #should include game code in lobby name
    path('setting_task',views.lobby_view,name='setting_task'),
    path('game/join_lobby/<str:game_code>/', views.join_lobby, name='join_lobby'),
    path('submit_task',views.submit_task,name='submit_task'),
    path('take_picture',views.take_picture,name='take_picture'),
    path('game/', views.members, name='game'),
    path('game_lobby',views.lobby_view,name='lobby_view'), #should include game code in lobby name

    path('', views.members, name='game'),
]
