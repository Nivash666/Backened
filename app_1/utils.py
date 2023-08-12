from jose import jwt
import requests

#def validate_cognito_token(token):
#    # Step 1: Verify the token signature
#    # You'll need to retrieve the public keys from Cognito to verify the token's signature.
#    # You can use the AWS Cognito JWKS endpoint to fetch the public keys.
#    jwks_url = 'https://cognito-idp.us-east-1.amazonaws.com/us-east-1_LsUhND2zs/.well-known/jwks.json'
#    response = requests.get(jwks_url)
#    jwks = response.json()
#
#    headers = jwt.get_unverified_header(token)
#    kid = headers['kid']
#    key = None
#
#    for jwk in jwks['keys']:
#        if jwk['kid'] == kid:
#            key = jwk
#            break
#
#    if key is None:
#        return False
#
#    # Step 2: Verify the token claims and signature
#    try:
#        claims = jwt.decode(token, key, algorithms=['RS256'], audience='7g2af98fpbih3tgb28btf3vnkq')
#        # You can add additional checks for the token claims here if needed.
#        # For example, you can check the token's expiration time (exp claim).
#
#        # If all checks pass, return True
#        return True
#
#    except jwt.JWTError:
#        # If any verification fails, return False
#        return False
#




# utils.py

import requests
from jose.backends import RSAKey
from jose.constants import ALGORITHMS
from jose.jwt import decode

def verify_cognito_token(token):
    jwks_url = f'https://cognito-idp.us-east-1.amazonaws.com/us-east-1_LsUhND2zs/.well-known/jwks.json'
    jwks_data = requests.get(jwks_url).json()
    
    rsa_key = RSAKey(key=jwks_data['keys'][0], algorithms=ALGORITHMS.RS256)
    payload = decode(token, rsa_key, options={'verify_aud': False})
    
    return payload
