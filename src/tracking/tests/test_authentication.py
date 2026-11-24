from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class AuthenticationApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user",
            password="test-password",
            first_name="Test",
        )
        self.client = APIClient(enforce_csrf_checks=True)
        csrf_response = self.client.get(reverse("api_auth_csrf"))
        self.csrf_headers = {"HTTP_X_CSRFTOKEN": csrf_response.data["csrfToken"]}

    def test_browser_login_sets_httponly_cookie_and_me_returns_identity(self):
        response = self.client.post(
            reverse("api_auth_login"),
            {"username": "test-user", "password": "test-password"},
            format="json",
            **self.csrf_headers,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "user": {
                    "id": self.user.pk,
                    "username": "test-user",
                    "first_name": "Test",
                }
            },
        )
        self.assertTrue(response.cookies["auth_token"]["httponly"])
        self.assertNotIn("token", response.data)

        me_response = self.client.get(reverse("api_auth_me"))

        self.assertEqual(me_response.status_code, 200)
        self.assertEqual(me_response.data["user"]["id"], self.user.pk)

    def test_native_login_returns_token_and_me_accepts_it(self):
        response = self.client.post(
            reverse("api_auth_token"),
            {"username": "test-user", "password": "test-password"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        token_key = response.data["token"]
        me_response = self.client.get(
            reverse("api_auth_me"),
            HTTP_AUTHORIZATION=f"Token {token_key}",
        )

        self.assertEqual(me_response.status_code, 200)
        self.assertEqual(me_response.data["user"]["id"], self.user.pk)

    def test_invalid_credentials_return_generic_error(self):
        response = self.client.post(
            reverse("api_auth_login"),
            {"username": "test-user", "password": "wrong-password"},
            format="json",
            **self.csrf_headers,
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"detail": "Invalid credentials."})

    def test_current_user_requires_authentication(self):
        response = self.client.get(reverse("api_auth_me"))

        self.assertEqual(response.status_code, 401)

    def test_logout_deletes_token_and_clears_cookie(self):
        self.client.post(
            reverse("api_auth_login"),
            {"username": "test-user", "password": "test-password"},
            format="json",
            **self.csrf_headers,
        )
        token = Token.objects.get(user=self.user)

        response = self.client.post(
            reverse("api_auth_logout"),
            format="json",
            **self.csrf_headers,
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.cookies["auth_token"].value, "")
        self.assertFalse(Token.objects.filter(pk=token.pk).exists())
        self.assertEqual(self.client.get(reverse("api_auth_me")).status_code, 401)

    def test_cookie_logout_requires_csrf_token(self):
        self.client.post(
            reverse("api_auth_login"),
            {"username": "test-user", "password": "test-password"},
            format="json",
            **self.csrf_headers,
        )

        response = self.client.post(reverse("api_auth_logout"), format="json")

        self.assertEqual(response.status_code, 403)
