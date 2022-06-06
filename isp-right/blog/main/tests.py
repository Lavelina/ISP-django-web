from django.test import TestCase
from django.urls import reverse
from main.models import *


class URLTests(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get("/registration/")

        self.assertEqual(response.status_code, 200)

    def test_login(self):
        login = self.client.login(username='test_user', password='testpass')
        self.client.logout()

    def test_main_view(self):
        response = self.client.get(f'')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_section_404(self):
        response = self.client.get("/section/66/")

        self.assertEqual(response.status_code, 404)

