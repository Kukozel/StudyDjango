from django.shortcuts import render,redirect
from lists.models import List
from lists.forms import ExistingListItemForm,ItemForm
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth import authenticate,login

# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        return render(request,'home.html',{'form':ItemForm()})
    return render(request, 'passError.html', {'message': 'Sign to Start!'})
def view_list(request,list_id):
    if request.user.is_authenticated:
        list_=List.objects.get(id=list_id)
        form=ExistingListItemForm(for_list=list_)
        if request.method == 'POST':
            form=ExistingListItemForm(for_list=list_,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(list_)
        return render(request, 'list.html', {'list': list_,'form':form})
    return render(request, 'passError.html', {'message': 'Authenticate Error!'})

def new_list(request):
    if request.user.is_authenticated:
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
    return render(request, 'passError.html', {'message': 'Authenticate Error!'})

def login_page(request):
    if request.method=='POST':
        user = authenticate(email=request.POST['email'],password=request.POST['password'])
        if (user):
            login(request, user)
            return render(request, 'home.html', {'form': ItemForm()})
        return render(request,'passError.html',{'message':'Email or Password Error!'})
    return render(request,'login.html')

def my_lists(request,email):
    if request.user.is_authenticated:
        owner = request.user
        return render(request, 'my_lists.html', {'owner': owner})
    return render(request,'passError.html',{'message':'Login Failer!'})


def register(request):
    if request.method=='POST':
        if request.POST['email'].strip() == '':
            return render(request, 'passError.html', {'message': "Email Can't be empty!"})
        if request.POST['password'].strip() == '':
            return render(request, 'passError.html', {'message': "Password Can't be empty!"})
        try:
            user = User.objects.get(email=request.POST['email'])
            return render(request, 'passError.html',{'message':'User Exist! Register Error!'})
        except User.DoesNotExist:
            if request.POST['password'] != request.POST['password_re']:
                return render(request,'passError.html',{'message':'Repeat Password Error!'})
            User.objects.create(email=request.POST['email'],password=request.POST['password'])
            return render(request,'passError.html',{'message':'Register Success!You Can Login Now!'})
    return render(request,'register.html')