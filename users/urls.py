from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import DashboardView
from django.contrib.auth.decorators import login_required
from django.conf.urls import url 

from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('register/', views.register, name='register'),
    #path('profile/', views.profile, name='profile'),
    #path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
   # path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    #path('logini/', views.login_user, name='login_user'),
    path('create/', views.enregistrer, name='create'),
   # url(r'^login/$', view=LoginView.as_view(template_name = "login.html"),name="login"),
  #  url(r'^dashboard/$', view=DashboardView.as_view(),name="dashboard"),
    #url(r'^logout/$', view=LogoutView.as_view(),name="logout1"),
    url(r'^deconnexion/$', views.deconnexion,name="logout")
]