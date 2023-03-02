from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('create_lobby', views.create_lobby, name='create_lobby'),
    path('add_lobby',views.add_lobby ,name='add_lobby'),
    path('get_game_data', views.get_game_data, name='get_game_data'),
    path('lobby',views.lobby_view,name='lobby_view'), #should include game code in lobby name
    path('setting_task',views.set_task_view,name='setting_task'),
    path('results',views.results_view,name='results'),
    path('join_lobby',views.lobby_view,name='join_lobby'),
    path('game/', views.members, name='game'),

    path('', views.members, name='game'),
]
