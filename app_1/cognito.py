# myapp/cognito.py

import requests
from jose import jwk, jwt
from django.conf import settings

def fetch_jwks_from_cognito(region, user_pool_id):
    cognito_jwks_url = f"https://cognito-idp.{region}.amazonaws.com/{user_pool_id}/.well-known/jwks.json"
    response = requests.get(cognito_jwks_url)

    if response.status_code == 200:
        jwks_json = response.json()
        keys = [jwk.construct(key) for key in jwks_json['keys']]
        return keys
    else:
        raise Exception("Failed to fetch JWKS from Cognito")

def get_jwt_claims(token):
    # Your implementation for JWT verification and claims extraction here
    keys = fetch_jwks_from_cognito(
        region=settings.COGNITO_CONFIG['region'],
        user_pool_id=settings.COGNITO_CONFIG['user_pool_id']
    )

    try:
        headers = jwt.get_unverified_headers(token)
        kid = headers["kid"]

        key_index = -1
        for i in range(len(keys)):
            if kid == keys[i].kid:
                key_index = i
                break

        if key_index == -1:
            raise Exception("Public key not found in jwks.json")

        public_key = keys[key_index].public_key
        claims = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            audience=settings.COGNITO_CONFIG['app_client_id'],
        )

        return claims
    except jwt.ExpiredSignatureError:
        raise Exception("Token is expired")
    except jwt.InvalidAudienceError:
        raise Exception("Token was not issued for this audience")
    except jwt.InvalidTokenError:
        raise Exception("Invalid auth token")
