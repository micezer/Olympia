# Django core
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages

# Autenticación
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Modelos y formularios propios
from .models import UserProfile, Service
from .forms import (
    UserForm,
    MyUserCreationForm,
    UserProfileForm
)


def loginPage(request):
    if request.user.is_authenticated:
        logger.debug(f"User {request.user.username} attempted to access login page while already authenticated")
        return redirect('home')

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"Successful login for user: {user.username} (IP: {request.META.get('REMOTE_ADDR')})")
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            logger.warning(
                f"Failed login attempt for username: {request.POST.get('username', '').strip()} "
                f"(IP: {request.META.get('REMOTE_ADDR')})"
            )

    context = {
        'page': 'login',
        'form': form
    }
    return render(request, 'base/login_register.html', context)


import logging
logger = logging.getLogger(__name__)

# views.py
from django.shortcuts import render
def offline(request):
    return render(request, 'offline.html')

def inscripciones_view(request):
    return render(request, 'base/inscripciones.html')

def cantera_view(request):
    return render(request, 'base/cantera.html')

def download_view(request):
    return render(request, 'base/download.html')
def about_view(request):
    return render(request, 'base/about.html')

from .forms import CustomUserCreationForm

def registerPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect page
    else:
        form = CustomUserCreationForm()
    return render(request, 'base/login_register.html', {'form': form})



def logoutUser(request):
    logout(request)
    return redirect('home')

from django.http import JsonResponse

def home(request):
    if request.user.is_authenticated:
        user_services = request.user.userprofile.services.all()
    else:
        user_services = None
    return render(request, 'base/home.html', {'user_services': user_services})



def userProfile(request, user):
    profile_user = get_object_or_404(User, username=user)
    
    
    recent_messages = messages[:3]
    
    context = {
        'profile_user': profile_user,
    }
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', user=user.username)

    return render(request, 'base/update-user.html', {'form': form})

