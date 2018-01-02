from django.contrib.auth import get_user_model

User=get_user_model()

PERSONA_VARIFY_URL='/accounts/login'

class PersonaAuthenticationBackend(object):

    def authenticate(self,email,password):
        self.email=email;
        self.password=password;
        try:
            return User.objects.get(email=self.email,password=self.password)
        except User.DoesNotExist:
            return None

    def get_user(self,email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None