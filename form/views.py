from pyexpat.errors import messages

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render,redirect
from form.models import Student
from .forms import NewUserForm
from django.http import HttpResponse


def form(request):
    return render(request,'form/form.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})