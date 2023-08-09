#from functools import wraps
#from django.http import HttpResponseForbidden
#from .utils import validate_cognito_token
#
#def cognito_jwt_auth_required(view_func):
#    @wraps(view_func)
#    def wrapped_view(request, *args, **kwargs):
#        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]  # Assuming the token is passed in the Authorization header as "Bearer <token>"
#        
#        if not validate_cognito_token(token):
#            return HttpResponseForbidden("Invalid Cognito token")
#        
#        return view_func(request, *args, **kwargs)
#    
#    return wrapped_view
#
#
#
##from functools import wraps
##from django.http import HttpResponseForbidden
##from .utils import validate_cognito_token
#
#def cognito_jwt_auth_required(view_func):
#    @wraps(view_func)
#    def wrapped_view(request, *args, **kwargs):
#        authorization_header = request.META.get('HTTP_AUTHORIZATION')
#        
#        if not authorization_header:
#            return HttpResponseForbidden("Missing Authorization header")
#        
#        try:
#            token = authorization_header.split(' ')[1]  # Assuming the token is passed in the Authorization header as "Bearer <token>"
#        except IndexError:
#            return HttpResponseForbidden("Invalid Authorization header format")
#        
#        if not validate_cognito_token(token):
#            return HttpResponseForbidden("Invalid Cognito token")
#        
#        return view_func(request, *args, **kwargs)
#    
#    return wrapped_view
#










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
#        # You can also return a user object here if needed.
#        # For example, if you have user information in the JWT claims, you can create or retrieve a user based on that information.
#
#        return None
#




import boto3
from django.http import JsonResponse

COGNITO_USER_POOL_ID = 'us-east-1_LsUhND2zs'
COGNITO_APP_CLIENT_ID = '7g2af98fpbih3tgb28btf3vnkq'
COGNITO_REGION='us-east-1'
#def validate_aws_cognito_token(view_func):
#    def _wrapped_view(request, *args, **kwargs):
#        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
#
#        if not token:
#            return JsonResponse({'error': 'Token not found'}, status=401)
#
#        try:
#            client = boto3.client('cognito-idp', region_name=COGNITO_REGION)
#            response = client.get_user(AccessToken=token)
#            # Additional checks if needed (e.g., user roles, attributes)
#        except client.exceptions.NotAuthorizedException:
#            return JsonResponse({'error': 'Invalid token'}, status=401)
#        except client.exceptions.InvalidParameterException:
#            return JsonResponse({'error': 'Invalid token'}, status=401)
#        except client.exceptions.UserNotFoundException:
#            return JsonResponse({'error': 'User not found'}, status=401)
#        except Exception as e:
#            return JsonResponse({'error': 'Something went wrong'}, status=500)
#
#        # If token is valid, proceed to the view
#        return view_func(request, *args, **kwargs)
#
#    return _wrapped_view

#from functools import wraps
#
#def requires_authentication(view_func):
#    @wraps(view_func)
#    def wrapped_view(request,*args,**kwargs):
#        if not request.user.is_authenticated:
#            return JsonResponse({'error':'Authentication Required'},status=401)
#
#        return view_func(request,*args,**kwargs)
#    return wrapped_view




from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def aws_cognito_token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')

        if not auth_header:
            return Response({'message': 'Authentication credentials were not provided'}, status=status.HTTP_401_UNAUTHORIZED)

        parts = auth_header.split(' ')

        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return Response({'message': 'Invalid authorization header format'}, status=status.HTTP_401_UNAUTHORIZED)

        token = parts[1]
        user_data = validate_cognito_token(token)

        if not user_data:
            return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        return view_func(request, *args, **kwargs)

    return _wrapped_view




