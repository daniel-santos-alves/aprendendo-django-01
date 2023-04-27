import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_sucessfully(self):
        string_password = "pass123"
        user = User.objects.create_superuser(
            username="my_user", password=string_password
        )  # noqa E501

        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse("authors:login"))

        # Usuário ver o formulário
        form = self.browser.find_element(By.CLASS_NAME, "main-form")
        username_field = self.get_by_placeholder(form, "Type your username")
        password_field = self.get_by_placeholder(form, "Type your password")

        # Usuário digita usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Usuário envia o formulário
        form.submit()

        # Usuário ver a mensagem de login com sucesso e seu nome
        self.assertIn(
            f"Your are logged in with {user.username}.",
            self.browser.find_element(By.TAG_NAME, "body").text,
        )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url + reverse("authors:login_create")
        )  # noqa E501

        self.assertIn(
            "Not Found", self.browser.find_element(By.TAG_NAME, "body").text
        )  # noqa E501
