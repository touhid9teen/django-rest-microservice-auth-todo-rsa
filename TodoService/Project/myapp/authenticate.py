from rest_framework.authentication import BaseAuthentication
from .todo_service import fetch_public_key
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
import jwt

class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if auth_header:
            token = self.get_token_from_header(auth_header)
            if token:
                try:
                    payload = self.decode_token(token)
                    return (AnonymousUser(), payload)
                except jwt.ExpiredSignatureError:
                    raise PermissionDenied('Token has expired')
                except jwt.InvalidTokenError:
                    raise PermissionDenied('Invalid token')

        return (AnonymousUser(), None)

    def get_token_from_header(self, auth_header):
        parts = auth_header.split()
        if parts[0].lower() != 'bearer':
            raise PermissionDenied('Authorization header must start with Bearer')
        if len(parts) == 1:
            raise PermissionDenied('Token not provided')
        elif len(parts) > 2:
            raise PermissionDenied('Authorization header must be Bearer token')
        return parts[1]

    def decode_token(self, token):
        try:
            public_key = fetch_public_key()
            payload = jwt.decode(token, public_key, algorithms=['RS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise PermissionDenied('Token has expired')
        except jwt.InvalidTokenError:
            raise PermissionDenied('Token is invalid')
