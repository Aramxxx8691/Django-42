from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('favourites', views.favourites, name='favourites'),
    path('publications', views.publications, name='publications'),
    path('publish/', views.article_publish, name='article_publish'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('favorite/<int:article_id>/<str:action>/', views.favorite, name='favorite'),
    path('set-language/<str:lang_code>/', views.set_language, name='set_language'),
]
