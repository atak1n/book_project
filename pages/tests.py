from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class HomePageTest(SimpleTestCase):

    def test_HP_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_HP_BY_NAME_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_HP_RIGHT_TEMPLATE(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTest(TestCase):

    username = 'testuser'
    email = 'testuser@ya.ru'
    password = 'password11'
    year = 2077

    def test_SIGNUP_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )

        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        # self.assertEqual(get_user_model().objects.all()[0].year, self.year)
        # self.assertEqual(get_user_model().objects.all()[0].password, self.password)


    def test_SIGNUP_status_code(self):
        response = self.client.get('/accounting/signup/')
        self.assertEqual(response.status_code, 200)

    def test_SIGNUP_BY_NAME_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_SIGNUP_RIGHT_TEMPLATE(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')



