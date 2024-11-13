from django.urls import path
from . import views

urlpatterns = [   
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('favourites', views.FavouritesView.as_view(), name='favourites'),
    path('publications', views.PublicationsView.as_view(), name='publications'),
    path('publish/', views.ArticlePublishView.as_view(), name='article_publish'),
    path('article/<int:id>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', views.ArticleEditView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('favorite/<int:article_id>/<str:action>/', views.FavoriteView.as_view(), name='favorite'),
    path('set-language/<str:lang_code>/', views.SetLanguageView.as_view(), name='set_language'),
]
