from django.contrib.auth.models import User
from rest_framework import authentication
from .exceptions import NoAuthToken, InvalidAuthToken, FirebaseError
from django.contrib.auth.models import User
import firebase_admin as admin
import firebase_admin.auth as auth


class FirebaseAuthentication(authentication.BaseAuthentication):
    
    saved_state = False
    @classmethod
    def authenticate(cls, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()
        try:
            user= User.objects.get(username=uid)
            cls.saved_state = True 
        except User.DoesNotExist:
            user =  User.objects.create(username=uid)
            user.save()

        return (user,None)

