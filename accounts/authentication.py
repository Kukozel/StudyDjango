from django.contrib.auth import get_user_model

User=get_user_model()

PERSONA_VARIFY_URL='/accounts/login'

class PersonaAuthenticationBackend(object):

    def authenticate(self,assertion):
        eamil=assertion
        try:
            return User.objects.get(email=eamil)
        except User.DoesNotExist:
            return User.objects.create(email=eamil)

    def get_user(self,email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None