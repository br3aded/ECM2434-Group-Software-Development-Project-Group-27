from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from game.models import Game, AppUser , Group
from datetime import datetime
from django.utils import timezone

class CreateLobbyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('game:create_lobby')
        self.user = User.objects.create_user(username='testuser', password='password')
        
    def test_create_lobby_view_should_return_200_status_code_for_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
    def test_create_lobby_view_should_redirect_to_login_for_unauthenticated_user(self):
        response = self.client.get(self.url)
        redirect_url = f'/login/?next={self.url}'
        self.assertRedirects(response, redirect_url)

class AddLobbyViewTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass123'
        self.user = User.objects.create_user(
            self.username, password=self.password)
        self.user.save()

        # Create AppUser object with points value
        self.app_user = AppUser.objects.create(base_user=self.user, points=0)

        self.add_lobby_url = reverse('game:add_lobby')

    def test_add_lobby_view_should_redirect_to_login_for_unauthenticated_user(self):
        response = self.client.get(self.add_lobby_url)
        self.assertRedirects(
            response, f'/login/?next={self.add_lobby_url}')

    def test_add_lobby_should_create_new_game_and_redirect_to_lobby_view(self):
        self.client.force_login(self.user)

        data = {
            'lobby name': 'Test Lobby',
            'num of players': 4,
            'num of rounds': 5,
        }

        response = self.client.post(self.add_lobby_url, data=data)

        self.assertRedirects(response, reverse('game:lobby_view'))

        # check that a new game has been created with the correct data
        new_game = Game.objects.get(game_name='Test Lobby')
        self.assertEqual(new_game.hosting_group.group_leader, self.app_user)
        self.assertEqual(new_game.game_state, 0)
        self.assertEqual(new_game.keeper_id, self.app_user)
        self.assertEqual(new_game.start_datetime.date(), datetime.now().date())

class MembersViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
    def test_members_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('game:game'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/join_lobby.html')
        self.assertEqual(response.context['username'], 'testuser')
        
    def test_members_view_with_unauthenticated_user(self):
        response = self.client.get(reverse('game:game'))
        self.assertRedirects(response, '/login/?next=/game/')