from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bosozoku.accounts.forms import LoginForm, RegisterForm, ProfileForm
from bosozoku.accounts.models import Profile
from bosozoku.events.models import Event


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_events = Event.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'events': user_events,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)


@login_required
def list_profiles(request):
    all_profiles = Profile.objects.all()

    context = {
        'profiles': all_profiles,
    }

    return render(request, 'accounts/profile_list.html', context)
