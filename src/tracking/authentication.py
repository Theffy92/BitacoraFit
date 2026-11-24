from django.middleware.csrf import CsrfViewMiddleware
from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

AUTH_TOKEN_COOKIE_NAME = "auth_token"


class _CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        return reason


class CookieTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        key = request.COOKIES.get(AUTH_TOKEN_COOKIE_NAME)
        if not key:
            return None

        try:
            token = Token.objects.select_related("user").get(key=key)
        except Token.DoesNotExist as exc:
            raise AuthenticationFailed("Invalid token.") from exc

        self.enforce_csrf(request)
        return token.user, token

    def enforce_csrf(self, request):
        check = _CSRFCheck(lambda request: None)
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            raise PermissionDenied(f"CSRF Failed: {reason}")
