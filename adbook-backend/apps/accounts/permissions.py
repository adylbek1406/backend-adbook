from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsOwnDevice(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class HasValidOTP(permissions.BasePermission):
    def has_permission(self, request, view):
        otp_code = request.data.get('otp_code')
        return bool(otp_code)

