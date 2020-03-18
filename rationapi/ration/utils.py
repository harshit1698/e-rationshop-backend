import datetime
import warnings

from django.conf import settings
from django.utils import timezone
from ration.models import *
from rest_framework_jwt.compat import get_username_field, get_username

import jwt
import uuid
import warnings

from django.contrib.auth import get_user_model

from calendar import timegm
# from datetime import datetime

from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings
expiry=settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token,user=None,request=None):

    role=Account_table.objects.get(auth_id=user).role_id.id
    is_verified =Account_table.objects.get(auth_id=user).verified

    return{'token':token,'user':user.username,'role':role,'is_verified':is_verified,'expiry':timezone.now()+expiry-datetime.timedelta(seconds=200)}


def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )

    payload = {
        'user_id': user.pk,
        'username': username,
        'exp': timezone.now()+expiry
    }
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload
