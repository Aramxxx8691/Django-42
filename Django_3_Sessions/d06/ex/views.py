
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils import timezone
from datetime import timedelta
from random import choice
from .models import Tip, Vote
from .forms import TipForm

# Create your views here.
def home(request):
    current_time = timezone.now()
    if request.user.is_authenticated:
        username = request.user.username
        tips = Tip.objects.all()
    else:
        if 'username' in request.COOKIES and 'username_expiry' in request.COOKIES:
            expiry_time = timezone.datetime.fromisoformat(request.COOKIES['username_expiry'])
            if current_time < expiry_time:
                username = request.COOKIES['username']
            else:
                username = choice(settings.USERNAMES)
                expiry_time = current_time + timedelta(seconds=42)
                response = render(request, 'ex/home.html', {'username': username, 'tips': [], 'form': None})
                response.set_cookie('username', username, max_age=42)
                response.set_cookie('username_expiry', expiry_time.isoformat(), max_age=42)
                return response
        else:
            username = choice(settings.USERNAMES)
            expiry_time = current_time + timedelta(seconds=42)
            response = render(request, 'ex/home.html', {'username': username, 'tips': [], 'form': None})
            response.set_cookie('username', username, max_age=42)
            response.set_cookie('username_expiry', expiry_time.isoformat(), max_age=42)
            return response
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                messages.success(request, "Tip created successfully!")
                return redirect('home')
        else:
            form = TipForm()
        tips = Tip.objects.all()
    else:
        form = None
        tips = []
    return render(request, 'ex/home.html', {'username': username, 'tips': tips, 'form': form})

@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    vote, created = Vote.objects.get_or_create(user=request.user, tip=tip)
    if vote.vote_type == Vote.UPVOTE:
        vote.delete()
        tip.upvotes -= 1
        tip.author.profile.reputation -= 5
    elif vote.vote_type == Vote.DOWNVOTE:
        vote.vote_type = Vote.UPVOTE
        vote.save()
        tip.upvotes += 1
        tip.downvotes -= 1
        tip.author.profile.reputation += 7
    else:
        vote.vote_type = Vote.UPVOTE
        vote.save()
        tip.upvotes += 1
        tip.author.profile.reputation += 5
    tip.author.profile.save()
    tip.save()
    return redirect('home')

@login_required
def downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    if request.user.profile.reputation < 15:
        messages.error(request, "You need at least 15 reputation points to downvote.")
        return redirect('home')
    if request.user == tip.author:
        messages.error(request, "You can't downvote your own tip.")
        return redirect('home')
    vote, created = Vote.objects.get_or_create(user=request.user, tip=tip)
    if vote.vote_type == Vote.DOWNVOTE:
        # User is removing their downvote
        vote.delete()
        tip.downvotes -= 1
        tip.author.profile.reputation += 2
    elif vote.vote_type == Vote.UPVOTE:
        # Changing an upvote to a downvote
        vote.vote_type = Vote.DOWNVOTE
        vote.save()
        tip.downvotes += 1
        tip.upvotes -= 1
        tip.author.profile.reputation -= 7  # Net change for switching from upvote to downvote
    else:
        # New downvote
        vote.vote_type = Vote.DOWNVOTE
        vote.save()
        tip.downvotes += 1
        tip.author.profile.reputation -= 2  # Reputation change for a new downvote

    # Save the updated profiles and tips
    tip.author.profile.save()
    tip.save()
    messages.success(request, "Downvote applied successfully.")
    return redirect('home')


@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user == tip.author or request.user.profile.reputation >= 30:
        if request.method == 'POST':
            reputation_deduction = (tip.upvotes * 5) + (tip.downvotes * 2)
            request.user.profile.reputation -= reputation_deduction
            request.user.profile.save()
            tip.delete()
            return redirect('home')
    else:
        return HttpResponseForbidden("You need at least 30 reputation points to delete tips.")
    return redirect('home')

@login_required
def tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('home')
    else:
        form = TipForm()
    return render(request, 'ex/create_tip.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return render(request, 'ex/login.html', {'username': username})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            response = redirect('home')
            response.delete_cookie('username')
            response.delete_cookie('username_expiry')
            return response
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'ex/login.html', {'username': username})
    return render(request, 'ex/login.html')

def logout(request):
    auth_logout(request)
    response = redirect('home')
    response.delete_cookie('username')
    response.delete_cookie('username_expiry')
    return response

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'ex/register.html', {'form': form})
