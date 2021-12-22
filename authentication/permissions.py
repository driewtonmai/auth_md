from rest_framework import permissions
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import UntypedToken, AccessToken


class IsDoctorUser(permissions.BasePermission):
    """Doctors verification based on token payloads."""

    def has_permission(self, request, view):
        token = request.auth
        try:
            decoded_token = UntypedToken(str(token))
        except TokenError:
            return

        if decoded_token.get('is_doctor'):
            print(decoded_token.get('is_doctor'))
            return True


