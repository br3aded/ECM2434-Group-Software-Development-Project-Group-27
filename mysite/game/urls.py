from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('add_lobby',views.add_lobby ,name='add_lobby'),
    path('lobby/<str:game_code>',views.lobby_view,name='lobby_view'), 
    path('setting_task/<str:game_code>',views.set_task_view,name='setting_task_view'),
    path('set_task/<str:game_code>', views.set_task , name = 'set_task'),
    path('add_user', views.add_user, name='add_user'),
    path('submit_task/<str:game_code>',views.submit_task,name='submit_task'),
    path('take_picture/<str:game_code>',views.take_picture,name='take_picture'),
    path('test',views.test,name='test'),
    path('game/', views.members, name='game'),
    path('player_lobbys', views.player_lobbys,name='player_lobbys'),
    path('', views.members, name='game'),
    path('end_game', views.end_game, name='end_game'),
    path('inc_gamestate', views.inc_gamestate, name='inc_gamestate'),
     path('waiting_for_response', views.inc_gamestate, name='waiting_for_response'),

    #urls with <str:game_code> display the game code of the game currently being played
]
