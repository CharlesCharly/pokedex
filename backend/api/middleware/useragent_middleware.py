from django.http import HttpResponseForbidden

class UserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for the custom header indicating a front-end request
        is_frontend_request = request.META.get('HTTP_X_FRONTEND_REQUEST', '') == 'true'

        # Check if it's not a front-end request
        if not is_frontend_request:
          return HttpResponseForbidden("Access denied")

        # If the user agent is not blocked, continue the request
        response = self.get_response(request)
        return response
