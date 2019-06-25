from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserCreationForm, UserLoginForm
User = get_user_model()
@login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated():
        print(request.user.profile.city)
    return render(request, "home.html", {})

def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    title = "User Register"
    if form.is_valid():
        form.save()
        print("user created")
        return HttpResponseRedirect("/login")
    return render(request, "accounts/register.html", {'form':form, 'title':title})

def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    title = "User Login" 
    if form.is_valid():
        #form.save()
        
        username = form.cleaned_data.get("username")
        user_obj = User.objects.get(username=username)
        print(f"{username} user logged")
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {'form':form, 'title':title})

def user_logout(request):
    logout(request)
    print(f"{request.user}  logged out")
    return HttpResponseRedirect("/login")
