from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
def persona_login(request):
    user=authenticate(assertion=request.POST['assertion'])
    if(user):
        login(request,user)
    return HttpResponse('okay')