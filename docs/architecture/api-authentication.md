# API authentication

The first React Native client flow uses Django REST Framework's database-backed
token authentication. The API exposes separate login transports so browser
JavaScript never needs access to a long-lived credential.

## Endpoints

All endpoints are under `/api/auth/`.

| Method and path | Purpose |
| --- | --- |
| `GET /csrf/` | Get a CSRF token before browser login or other cookie-authenticated writes. |
| `POST /login/` | Browser login. Accepts `username` and `password`, sets an HttpOnly token cookie, and returns basic user identity. |
| `POST /token/` | Native-client login. Accepts `username` and `password`, returns a token and basic user identity. |
| `GET /me/` | Return the authenticated user's ID, username, and first name. |
| `POST /logout/` | Delete the authenticated user's token and clear the browser token cookie. |

Invalid credentials receive the same generic `400` response regardless of
whether the username exists. Authentication credentials are not logged.

## Client credential handling

- **iOS and Android:** call `/token/`, store the returned token with the
  platform's secure credential store (for example, Keychain or Android
  Keystore-backed SecureStore), and send it as
  `Authorization: Token <token>`. Do not store it in AsyncStorage.
- **Browser:** first get a CSRF token from `/csrf/`, then submit `/login/` with
  the CSRF token in `X-CSRFToken` and credentialed CORS enabled. The API sets an
  HttpOnly, SameSite=Lax cookie scoped to `/api/auth/`; JavaScript cannot read
  the token. Send the CSRF header on cookie-authenticated write requests,
  including logout. Use HTTPS in production so the cookie is Secure.
- **Logout:** both transports invalidate the same per-user database token.
  Tokens are not rotated automatically; a subsequent login reuses a token if
  one remains, while logout deletes it.

The configured browser development origins are `localhost:3000` and
`localhost:8081`. Update both CORS and CSRF trusted origins for a deployed
frontend. The browser cookie design assumes a same-site frontend/API deployment;
cross-site deployments need an explicit cookie and CSRF policy.
