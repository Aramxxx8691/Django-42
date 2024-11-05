from django.conf import settings
from django.contrib import messages
from django.utils.translation import activate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponseRedirect
from .models import Article, UserFavouriteArticle
from .forms import ArticleForm

# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'ex/home.html', {'articles': articles})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('home')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            response = redirect('home')
            response.delete_cookie('username')
            response.delete_cookie('username_expiry')
            return response
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    return redirect('home')

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

def favourites(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'ex/favourites.html')

@login_required
def publications(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article published successfully.")
            return redirect('publications')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ArticleForm()
    articles = Article.objects.filter(author=request.user)
    return render(request, 'ex/publications.html', {'articles': articles, 'form': form})

@login_required
def article_publish(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article published successfully.")
            return redirect('publications')
    else:
        form = ArticleForm()
    return render(request, 'ex/article_publish.html', {'form': form})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'ex/article_detail.html', {'article': article})

@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        synopsis = request.POST.get('synopsis')
        content = request.POST.get('content')
        if not title or not synopsis or not content:
            messages.error(request, "All fields are required.")
        else:
            article.title = title
            article.synopsis = synopsis
            article.content = content
            article.save()
            messages.success(request, "Article updated successfully.")
            return redirect('publications')
    return render(request, 'ex/article_edit.html', {'article': article})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        article.delete()
        messages.success(request, "Article deleted successfully.")
        return redirect('publications')
    return redirect('publications')

def favorite(request, article_id, action):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authenticated'}, status=403)
    article = get_object_or_404(Article, id=article_id)
    if action == 'add':
        UserFavouriteArticle.objects.get_or_create(user=request.user, article=article)
    elif action == 'remove':
        UserFavouriteArticle.objects.filter(user=request.user, article=article).delete()
    return JsonResponse({'status': 'success'})

def favourites(request):
    if not request.user.is_authenticated:
        return redirect('login')
    favorites = UserFavouriteArticle.objects.filter(user=request.user).values_list('article', flat=True)
    articles = Article.objects.filter(id__in=favorites)
    return render(request, 'ex/favourites.html', {'favorites': articles})

def set_language(request, lang_code):
    if lang_code in dict(settings.LANGUAGES):
        activate(lang_code)
        request.session[settings.LANGUAGE_SESSION_KEY] = lang_code
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))