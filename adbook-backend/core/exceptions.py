from rest_framework import status
from rest_framework.exceptions import APIException

class Throttled(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = 'Request was throttled.'
    default_code = 'throttled'

class TokenBlacklisted(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Token has been blacklisted.'
    default_code = 'token_blacklisted'

class DeviceNotRecognized(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Device not recognized.'
    default_code = 'device_not_recognized'

