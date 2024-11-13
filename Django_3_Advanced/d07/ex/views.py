from django.http import Http404
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.utils.translation import activate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Article, UserFavouriteArticle
from .forms import ArticleForm

class HomeView(ListView):
    model = Article
    template_name = 'ex/home.html'
    context_object_name = 'articles'

class RegisterView(CreateView):
    model = Article
    template_name = 'ex/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('home')

class LoginView(TemplateView):
    template_name = 'ex/home.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
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

class LogoutView(TemplateView):
    template_name = 'ex/home.html'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        response = redirect('home')
        response.delete_cookie('username')
        response.delete_cookie('username_expiry')
        return response

class FavouritesView(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = 'ex/favourites.html'
    context_object_name = 'favorites'
    login_url = '/login/'

    def get_queryset(self):
        favorites = UserFavouriteArticle.objects.filter(user=self.request.user).values_list('article', flat=True)
        return Article.objects.filter(id__in=favorites)

class PublicationsView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(author=request.user)
        form = ArticleForm()
        return render(request, 'ex/publications.html', {'articles': articles, 'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article published successfully.")
            return redirect('publications')
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'ex/publications.html', {'form': form})

class ArticlePublishView(CreateView):
    model = Article
    template_name = 'ex/article_publish.html'
    form_class = ArticleForm
    success_url = reverse_lazy('publications')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, "Article published successfully.")
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'ex/article_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'

class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'ex/article_edit.html'
    form_class = ArticleForm
    context_object_name = 'article'
    login_url = '/login/'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Article updated successfully.")
        return redirect('publications')

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'ex/article_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('publications')
    login_url = '/login/'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("You do not have permission to delete this article.")
        return obj

class FavoriteView(View):
    def post(self, request, article_id, action):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Not authenticated'}, status=403)
        article = get_object_or_404(Article, id=article_id)
        if action == 'add':
            favorite, created = UserFavouriteArticle.objects.get_or_create(user=request.user, article=article)
            if created:
                return JsonResponse({'status': 'success', 'message': 'Article liked successfully.'})
            else:
                return JsonResponse({'status': 'already_exists', 'message': 'You already liked this article.'})
        elif action == 'remove':
            if UserFavouriteArticle.objects.filter(user=request.user, article=article).exists():
                UserFavouriteArticle.objects.filter(user=request.user, article=article).delete()
                return JsonResponse({'status': 'success', 'message': 'Article unliked successfully.'})
            else:
                return JsonResponse({'status': 'not_found', 'message': 'This article is not in your favorites.'})
        return JsonResponse({'status': 'error', 'message': 'Invalid action. Use "add" or "remove".'}, status=400)

class SetLanguageView(TemplateView):
    def get(self, request, lang_code, *args, **kwargs):
        if lang_code in dict(settings.LANGUAGES):
            activate(lang_code)
            request.session[settings.LANGUAGE_SESSION_KEY] = lang_code
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
