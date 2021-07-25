from django.contrib import admin
from django.urls import path, include
from releveCompte import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url 

from django.contrib.auth.views import LoginView


urlpatterns = [

    path('', views.tableau, name = 'infosignataire'),
    path('template', views.template),
    path('save', views.ajoutMontant,name='ajoutMontant'),
    #path('pdf', views.ViewPDF.as_view(),name='pdf'),
    path('imprimer', views.imprimer,name='imprimer'),
    path('input', views.simple_upload,name='input'),
    path('pdf', views.GeneratePdf.as_view(),name='input'),
    path('create-pdf', views.pdf_report_create,name='create-pdf'),
    #path('login', views.loginPage,name='login1'),
    #path('register', views.registerPage,name='register'),
    path('indexs', views.vuesecretaire,name='indexs'),
    path('indexc', views.vuechef,name='indexc'),
   



]