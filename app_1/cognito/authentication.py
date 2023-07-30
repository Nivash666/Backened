# myapp/cognito/authentication.py



import requests
from jwkest.jwk import KEYS

# myapp/cognito/authentication.py

import os
import time
import jwt
import requests
from jwt.utils import get_int_from_datetime, base64url_decode
from jwt.algorithms import get_default_algorithms
from django.conf import settings
from django.contrib.auth.models import User
from jose import jwk, jwt

class NoAuthToken(Exception):
    pass

class CognitoAuthenticationMixin:
    def get_auth_token(self, request):
        try:
            return request.META["HTTP_AUTHORIZATION"]
        except Exception:
            raise NoAuthToken()

    def get_jwt_claims(self, token):
        try:
            headers = jwt.get_unverified_headers(token)
            kid = headers["kid"]

            key_index = -1
            for i in range(len(keys)):
                if kid == keys[i]["kid"]:
                    key_index = i
                    break

            if key_index == -1:
                raise Exception("Public key not found in jwks.json")

            public_key = jwk.construct(keys[key_index])
            message, encoded_signature = str(token).rsplit(".", 1)
            decoded_signature = base64url_decode(encoded_signature.encode("utf-8"))

            if not public_key.verify(message.encode("utf8"), decoded_signature):
                raise Exception("Signature verification failed")

            claims = jwt.get_unverified_claims(token)
            ts = claims["exp"]
            os.environ["TZ"] = "Asia/Kolkata"
            time.tzset()

            if time.time() > claims["exp"]:
                raise Exception("Token is expired")
            if claims["aud"] != settings.COGNITO_CONFIG["7g2af98fpbih3tgb28btf3vnkq"]:
                raise Exception("Token was not issued for this audience")

            return claims
        except Exception as e:
            raise Exception("Invalid auth token")

    def authenticate(self, request):
        token = self.get_auth_token(request)
        try:
            claims = self.get_jwt_claims(token)
            if len(claims) > 0:
                user = User.objects.get(email=claims["email"])
                return user
            raise Exception("User not found")
        except User.DoesNotExist:
            raise Exception("User not found")
        except Exception as e:
            raise Exception("Invalid auth token")







def fetch_jwks_from_cognito():
    cognito_jwks_url = "https://cognito-idp.{region}.amazonaws.com/{userPoolId}/.well-known/jwks.json"
    region = "your_cognito_region"
    user_pool_id = "your_cognito_user_pool_id"

    url = cognito_jwks_url.format(region=region, userPoolId=user_pool_id)
    response = requests.get(url)

    if response.status_code == 200:
        jwks_json = response.json()
        keys = KEYS()
        keys.load_dict(jwks_json)
        return keys
    else:
        raise Exception("Failed to fetch JWKS from Cognito")
keys = fetch_jwks_from_cognito()