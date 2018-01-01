from django.shortcuts import render,redirect
from lists.models import Item,List
from lists.forms import ExistingListItemForm,ItemForm
from django.contrib.auth import get_user_model
User=get_user_model()
from accounts.authentication import PersonaAuthenticationBackend
from django.contrib.auth import authenticate,login

# Create your views here.
def home_page(request):
    return render(request,'home.html',{'form':ItemForm()})

def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    form=ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form=ExistingListItemForm(for_list=list_,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_,'form':form})

def new_list(request):
    form=ItemForm(data=request.POST)
    if form.is_valid():
        list_=List()
        if request.user.is_authenticated:
            list_.owner=request.user
        list_.save()
        form.instance.list=list_
        form.save()
        return redirect(list_)
    else:
        return render(request,'home.html',{'form':form})

def login_page(request):
    if request.method=='POST':
        user = authenticate(assertion=request.POST['email'])
        if (user):
            login(request, user)
        try:
            user=User.objects.get(email=request.POST['email'])
        except User.DoesNotExist:
            user=User.objects.create(email=request.POST['email'])
        return render(request,'home.html',{'form':ItemForm()})
    return render(request,'login.html')


def my_lists(request,email):
    owner=User.objects.get(email=email)
    return render(request,'my_lists.html',{'owner':owner})

def register(request):
    pass