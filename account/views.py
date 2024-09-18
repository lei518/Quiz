from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser, Profile
from .forms import UserRegistrationForm, ProfileForm

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('homepage')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': user_form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            profile = Profile.objects.get(user=user)
            if profile:
                login(request, user)
                return redirect('homepage')
            else:
                return redirect('create_profile')
    return render(request, 'accounts/login.html')

def create_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('homepage')
    else:
        profile_form = ProfileForm()
    return render(request, 'accounts/create_profile.html', {'form': profile_form})
