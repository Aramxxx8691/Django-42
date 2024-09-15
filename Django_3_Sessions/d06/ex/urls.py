from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('tip', views.tip, name='tip'),
    path('upvote/<int:tip_id>/', views.upvote_tip, name='upvote_tip'),
    path('downvote/<int:tip_id>/', views.downvote_tip, name='downvote_tip'),
    path('delete/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]
