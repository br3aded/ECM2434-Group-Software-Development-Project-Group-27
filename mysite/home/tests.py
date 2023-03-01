from django.test import TestCase, Client
from django.urls import reverse
from django.template import loader
from django.contrib.auth.models import User
from .models import AppUser
from django.contrib.auth import authenticate, login, logout


class AddUserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_user_url = reverse('home:add_user')
        self.login_url = reverse('home:login')
        self.user_data = {
            'Username': 'testuser',
            'Email': 'testuser@example.com',
            'Password': 'testpassword',
        }
        self.existing_user = User.objects.create_user(
            username='existinguser',
            email='existinguser@example.com',
            password='existingpassword'
        )

    def add_user(self):
        response = self.client.post(self.add_user_url, data=self.user_data)
        self.assertRedirects(response, self.login_url)
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(AppUser.objects.count(), 1)
        self.assertTrue(AppUser.objects.filter(base_user__username='testuser').exists())

class MembersViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_members_view_should_return_200(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

    def test_members_view_should_use_index_template(self):
        response = self.client.get(reverse('home:home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_members_view_should_return_correct_content(self):
        response = self.client.get(reverse('home:home'))
        expected_content = loader.render_to_string('index.html')
        self.assertContains(response, expected_content)

class LoginUserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_login_user_view_with_valid_credentials_should_redirect_to_game(self):
        response = self.client.post(reverse('home:login_user'), {'Username': 'testuser', 'Password': 'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('game:game'), fetch_redirect_response=False)

    def test_login_user_view_with_invalid_credentials_should_redirect_to_login(self):
        response = self.client.post(reverse('home:login_user'), {'Username': 'testuser', 'Password': 'wrongpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:login'), fetch_redirect_response=False)

class LogoutUserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_logout_user_view_should_redirect_to_home(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('home:logout_user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'), fetch_redirect_response=False)

    def test_logout_user_view_should_log_out_user(self):
        # Create a test user and log them in
        self.client.login(username='testuser', password='12345')

        # Make a GET request to the logout_user view
        response = self.client.get(reverse('home:logout_user'))

        # Check that the response status code is 302
        self.assertEqual(response.status_code, 302)

        # Check that the user is not logged in anymore
        self.client.logout()
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)
