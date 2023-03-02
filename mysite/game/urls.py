from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('add_lobby',views.add_lobby ,name='add_lobby'),
    path('get_game_data', views.get_game_data, name='get_game_data'),
    path('lobby',views.lobby_view,name='lobby_view'), #should include game code in lobby name
    path('setting_task',views.set_task_view,name='setting_task'),
    path('results',views.results_view,name='results'),
    path('join_lobby',views.lobby_view,name='join_lobby'),
    #path('check_code', views.check_code, name='check_code'),
    path('lobby/<str:game_code>/',views.lobby_view,name='lobby_view'), #should include game code in lobby name
    path('setting_task',views.lobby_view,name='setting_task'),
    path('game/join_lobby/<str:game_code>/', views.join_lobby, name='join_lobby'),
    path('game/', views.members, name='game'),
    path('player_lobbys', views.player_lobbys,name='player_lobbys'),
    path('', views.members, name='game'),
]
