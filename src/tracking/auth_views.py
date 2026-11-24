from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import AUTH_TOKEN_COOKIE_NAME


def _user_identity(user):
    return {
        "id": user.pk,
        "username": user.get_username(),
        "first_name": user.first_name,
    }


def _authenticate_credentials(request):
    credentials = request.data
    if not isinstance(credentials, dict):
        return None

    username = credentials.get("username")
    password = credentials.get("password")
    if not isinstance(username, str) or not isinstance(password, str):
        return None

    return authenticate(request, username=username, password=password)


class CsrfTokenView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"csrfToken": get_token(request)})


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        user = _authenticate_credentials(request)
        if user is None:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token, _ = Token.objects.get_or_create(user=user)
        response = Response({"user": _user_identity(user)})
        response.set_cookie(
            AUTH_TOKEN_COOKIE_NAME,
            token.key,
            httponly=True,
            secure=not settings.DEBUG,
            samesite="Lax",
            path="/api/auth/",
        )
        return response


class TokenLoginView(LoginView):
    authentication_classes = ()

    def post(self, request):
        user = _authenticate_credentials(request)
        if user is None:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": _user_identity(user)})


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"user": _user_identity(request.user)})


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.auth.delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie(
            AUTH_TOKEN_COOKIE_NAME,
            path="/api/auth/",
            samesite="Lax",
            secure=not settings.DEBUG,
        )
        return response
