from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token

class CustomUser:
    def __init__(self, token: Token):
        self.id = token.get('user_id')
        
        self.is_authenticated = True 
        
        self.is_staff = token.get('is_staff', False)
        self.is_superuser = token.get('is_superuser', False)

    @property
    def is_active(self):
        return True

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user = CustomUser(validated_token)
            return user
        except Exception:
            return AnonymousUser()
