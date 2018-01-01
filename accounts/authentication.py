import requests
from django.contrib.auth import get_user_model

User=get_user_model()

PERSONA_VARIFY_URL='/accounts/login'

class PersonaAuthenticationBackend(object):

    def authenticate(self,assertion):
        # response=requests.post(
        #     PERSONA_VARIFY_URL,
        #     data={'assertion':assertion,'email':assertion}
        # )
        # if response.ok and response.json()['status']=='okay':
        #     eamil=response.json()['email']
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