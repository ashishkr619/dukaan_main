import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import Account

"""
Identity customer using JWT or token which can be generated using his mobile number and a OTP
Bypass the actual OTP validation flow and issue a token on any random number & OTP combination
"""


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
    def authenticate(self, request):

        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        # auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            # Invalid token header. The Token string should not contain spaces. Do
            # not attempt to authenticate.
            return None
        # prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token. If not, throw an error.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception as e:
            print(e)
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = Account.objects.get(pk=payload['id'])
            print('user', user)
        except Account.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
