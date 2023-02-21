from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.members, name='home'),
    path('login/', views.login_view, name='login'),
    path('login/add_user',views.add_user, name='add_user'),
    path('login/user_login', views.login_user, name='login_user'),
]