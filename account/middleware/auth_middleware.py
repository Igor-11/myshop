from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
import json

class AuthMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response

    

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if 'user' not in request.session and not request.path.startswith('/account'):
           request.error = 403
        return None

            