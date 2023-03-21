from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('add_lobby',views.add_lobby ,name='add_lobby'),
    path('get_game_data', views.get_game_data, name='get_game_data'),
    path('lobby/<str:game_code>',views.lobby_view,name='lobby_view'), #should include game code in lobby name
    path('setting_task/<str:game_code>',views.set_task_view,name='setting_task_view'),
    path('set_task/<str:game_code>', views.set_task , name = 'set_task'),
    path('join_lobby', views.get_game_data, name='join_lobby'),
    path('submit_task/<str:game_code>',views.submit_task,name='submit_task'),
    path('take_picture/<str:game_code>',views.take_picture,name='take_picture'),
    path('test',views.test,name='test'),
    path('game/', views.members, name='game'),
    path('player_lobbys', views.player_lobbys,name='player_lobbys'),
    path('', views.members, name='game'),
]
