from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken, TokenError

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class WebSocketJWTAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        parsed_query_string = parse_qs(scope["query_string"])
        token = parsed_query_string.get(b"token")[0].decode("utf-8")

        try:
            access_token = AccessToken(token)
            scope["user"] = await get_user(access_token["user_id"])
        except TokenError:
            scope["user"] = AnonymousUser()

        return await self.app(scope, receive, send)
