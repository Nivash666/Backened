from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .utils import validate_cognito_token

class CognitoJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        if not token:
            return None

        if not validate_cognito_token(token):
            raise AuthenticationFailed("Invalid Cognito token")

        # If the token is valid, you can return a user object here if needed.
        # For example, if you have user information in the JWT claims, you can create or retrieve a user based on that information.
        # You can also attach the user to the request to access it in the views using request.user.

        return None
