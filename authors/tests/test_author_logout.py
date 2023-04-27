from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthorLogouTest(TestCase):
    def test_user_tries_to_logout_using_get_method(self):
        User.objects.create_superuser(username="my_user", password="my_pass")
        self.client.login(username="my_user", password="my_pass")

        response = self.client.get(reverse("authors:logout"), follow=True)

        self.assertIn(  # noqa E501
            "Invalid logout request", response.content.decode("utf-8")
        )

    def test_user_tries_to_logout_another_user(self):
        User.objects.create_superuser(username="my_user", password="my_pass")
        self.client.login(username="my_user", password="my_pass")

        response = self.client.post(
            reverse("authors:logout"),  # noqa E501
            data={"username": "another_user"},
            follow=True,
        )

        self.assertIn(  # noqa E501
            "Invalid logout user", response.content.decode("utf-8")
        )

    def test_user_can_logout_sucessfully(self):
        User.objects.create_superuser(username="my_user", password="my_pass")
        self.client.login(username="my_user", password="my_pass")

        response = self.client.post(
            reverse("authors:logout"),  # noqa E501
            data={"username": "my_user"},
            follow=True,
        )

        self.assertIn(
            "Logged out successfully", response.content.decode("utf-8")
        )  # noqa E501
