import boto3
from botocore.exceptions import ParamValidationError, NoCredentialsError
from django.conf import settings
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
class AWSCognitoTokenMixin:
    def validate_cognito_token(self, token):
        user_pool_id = settings.COGNITO_USER_POOL_ID
        region = settings.COGNITO_AWS_REGION

        client = boto3.client('cognito-idp', region_name=region)

        try:
            response = client.get_user(
                AccessToken=token,
                ClientId=settings.COGNITO_APP_CLIENT_ID
            )
            user_data = response['UserAttributes']
            return user_data
        except (ParamValidationError, NoCredentialsError, client.exceptions.NotAuthorizedException):
            return None
        except Exception as e:
            print(f"Token validation error: {e}")
            return None
    def aws_cognito_token_required(self, view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')

            if not auth_header:
                return Response({'message': 'Authentication credentials were not provided'}, status=status.HTTP_401_UNAUTHORIZED)

            parts = auth_header.split(' ')

            if len(parts) != 2 or parts[0].lower() != 'bearer':
                return Response({'message': 'Invalid authorization header format'}, status=status.HTTP_401_UNAUTHORIZED)

            token = parts[1]
            user_data = self.validate_cognito_token(token)

            if not user_data:
                return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

            return view_func(self, request, *args, **kwargs)

        return _wrapped_view
