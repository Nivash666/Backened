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




from functools import wraps
from django.http import HttpResponseForbidden
from .utils import validate_cognito_token

def cognito_jwt_auth_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        
        if not authorization_header:
            return HttpResponseForbidden("Missing Authorization header")
        
        try:
            token = authorization_header.split(' ')[1]  # Assuming the token is passed in the Authorization header as "Bearer <token>"
        except IndexError:
            return HttpResponseForbidden("Invalid Authorization header format")
        
        if not validate_cognito_token(token):
            return HttpResponseForbidden("Invalid Cognito token")
        
        return view_func(request, *args, **kwargs)
    
    return wrapped_view
