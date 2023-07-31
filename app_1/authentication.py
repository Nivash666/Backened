# myapp/authentication.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from .cognito import get_jwt_claims
from django.contrib.auth.models import User

class CognitoAuthenticationBackend(JWTAuthentication):
    def authenticate(self, request):
        authenticated_user = super().authenticate(request)

        if authenticated_user:
            token = request.auth
            try:
                claims = get_jwt_claims(token)
                if len(claims) > 0:
                    user = User.objects.get(email=claims["email"])
                    return user
            except User.DoesNotExist:
                pass
            except Exception:
                pass

        return None































#from rest_framework.authentication import BaseAuthentication
#from rest_framework.exceptions import AuthenticationFailed
#from .utils import validate_cognito_token
#
#class CognitoJWTAuthentication(BaseAuthentication):
#    def authenticate(self, request):
#        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
#
#        if not token:
#            return None
#
#        if not validate_cognito_token(token):
#            raise AuthenticationFailed("Invalid Cognito token")
#
#        # If the token is valid, you can return a user object here if needed.
#        # For example, if you have user information in the JWT claims, you can create or retrieve a user based on that information.
#        # You can also attach the user to the request to access it in the views using request.user.
#
#        return None
#
#











#from rest_framework_simplejwt.authentication import JWTAuthentication
#from rest_framework.exceptions import AuthenticationFailed
#
#class CustomJWTAuthentication(JWTAuthentication):
#    def authenticate(self, request):
#        try:
#            user = super().authenticate(request)
#        except AuthenticationFailed:
#            # Handle invalid or expired tokens
#            return None
#
#        if user is None:
#            # Handle anonymous user
#            return None
#
#        # Add custom logic here if needed
#        # For example, you can fetch the user from the database based on the JWT token claims.
#
#        return user


# myapp/authentication.py

#import os
#import time
#from jwt import PyJWKClient
#from jwt.utils import get_int_from_datetime
#from jwt.algorithms import get_default_algorithms
#from django.conf import settings
#from django.contrib.auth import authentication
#from app_1.models import UserModel  # Replace with your actual user model
#
## Your other imports and code for keys retrieval go here
#
## ... (previous code)
#
## Continue with the rest of the code in authentication.py
## You can copy the provided code and update UserModel with your actual user model.
#
#


# myapp/cognito/authentication.py

# myapp/cognito/authentication.py

#import os
#import time
#import jwt
#from jwt import PyJWKClient
#from jwt.algorithms import get_default_algorithms
#from django.conf import settings
#from app_1.models import UserModel
#from django.contrib.auth import authentication
#from jwt.utils import base64url_decode
#from jose import jwk, jwt
#
## Your other imports and code for keys retrieval go here
#
#class CognitoAuthenticationMixin:
#    def get_auth_token(self, request):
#        try:
#            return request.META["HTTP_AUTHORIZATION"]
#        except Exception:
#            raise NoAuthToken()
#
#    def get_jwt_claims(self, token):
#        try:
#            headers = jwt.get_unverified_headers(token)
#            kid = headers["kid"]
#
#            key_index = -1
#            for i in range(len(keys)):
#                if kid == keys[i]["kid"]:
#                    key_index = i
#                    break
#
#            if key_index == -1:
#                raise Exception("Public key not found in jwks.json")
#
#            public_key = jwk.construct(keys[key_index])
#            message, encoded_signature = str(token).rsplit(".", 1)
#            decoded_signature = base64url_decode(encoded_signature.encode("utf-8"))
#
#            if not public_key.verify(message.encode("utf8"), decoded_signature):
#                raise Exception("Signature verification failed")
#
#            claims = jwt.get_unverified_claims(token)
#            ts = claims["exp"]
#            os.environ["TZ"] = "Asia/Kolkata"
#            time.tzset()
#
#            if time.time() > claims["exp"]:
#                raise Exception("Token is expired")
#            if claims["aud"] != settings.COGNITO_CONFIG["7g2af98fpbih3tgb28btf3vnkq"]:
#                raise Exception("Token was not issued for this audience")
#
#            return claims
#        except Exception as e:
#            raise Exception("Invalid auth token")
#
#    def authenticate(self, request):
#        token = self.get_auth_token(request)
#        try:
#            claims = self.get_jwt_claims(token)
#            if len(claims) > 0:
#                user = UserModel.objects.get(email=claims["email"])
#                return user
#            raise Exception("User not found")
#        except UserModel.DoesNotExist:
#            raise Exception("User not found")
#        except Exception as e:
#            raise Exception("Invalid auth token")
#