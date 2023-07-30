# middleware.py

#from django_cognito_jwt import JSONWebTokenAuthentication
#from django.http import JsonResponse
#
#class CognitoTokenMiddleware:
#    def __init__(self, get_response):
#        self.get_response = get_response
#
#    def __call__(self, request):
#        # Authenticate the request using the JSONWebTokenAuthentication provided by django-cognito-jwt
#        auth = JSONWebTokenAuthentication()
#        request.user, request.token = auth.authenticate(request)
#
#        if request.user is None or request.token is None:
#            # Token authentication failed; return an unauthorized response
#            return JsonResponse({"error": "Unauthorized"}, status=401)
#
#        return self.get_response(request)
#


# myapp/middleware.py

from django.urls import reverse
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import MiddlewareMixin
from app_1.cognito.authentication import CognitoAuthenticationMixin, NoAuthToken


class CognitoAuthMiddleware(CognitoAuthenticationMixin, MiddlewareMixin):
    @staticmethod
    def get_auth_token(request):
        try:
            return request.META["HTTP_AUTHORIZATION"]
        except Exception:
            raise NoAuthToken()

    def process_request(self, request):
        if request.path.startswith(reverse("admin:index")):
            return None
        request.user = SimpleLazyObject(lambda: self.authenticate(request))




