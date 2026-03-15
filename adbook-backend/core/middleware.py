import redis
from django.conf import settings
from rest_framework.throttling import UserRateThrottle
from core.exceptions import Throttled

# rdb = redis.from_url(settings.REDIS_URL)

class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # JWT blacklist check (in auth backend)
        # Brute force protection
        response = self.get_response(request)
        return response

class ThrottleMiddleware:
    def __init__(self, get_response):
        self.throttle = UserRateThrottle()
        self.get_response = get_response

    def __call__(self, request):
        if self.throttle.allow_request(request, None):
            response = self.get_response(request)
        else:
            raise Throttled()
        return response

