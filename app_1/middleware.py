# middleware.py

from django_cognito_jwt import JSONWebTokenAuthentication
from django.http import JsonResponse

class CognitoTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Authenticate the request using the JSONWebTokenAuthentication provided by django-cognito-jwt
        auth = JSONWebTokenAuthentication()
        request.user, request.token = auth.authenticate(request)

        if request.user is None or request.token is None:
            # Token authentication failed; return an unauthorized response
            return JsonResponse({"error": "Unauthorized"}, status=401)

        return self.get_response(request)
