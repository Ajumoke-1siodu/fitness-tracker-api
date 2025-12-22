from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTests(APITestCase):
    def test_register_user(self):
        url = reverse("register")  # depends on how you wire the endpoint
        data = {
            "username": "geo",
            "email": "geo@example.com",
            "password": "pass123",
            "password2": "pass123"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, "geo")

