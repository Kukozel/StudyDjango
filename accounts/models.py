from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50,null=False,default='123456')
    last_login=models.DateTimeField(default=timezone.now)
    REQUIRED_FIELDS=()
    USERNAME_FIELD='email'

    is_anonymous=False

    is_authenticated=True