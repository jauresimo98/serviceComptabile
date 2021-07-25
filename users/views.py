 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from django.views.generic import TemplateView

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'users/login.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def login_user(request):
    if request.method == "POST":
     if request.is_ajax():
        username = request.POST['uname']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)

                return redirect('home')
            else:
                return render(request, 'index.html', {'error_message':'Account Deactivaated'})
        else:
            return render(request, 'index.html', {'error_message':'Invalid Login'})
    return render(request, 'login1.html')

def save_user(request):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            login = request.Utilisateur.get('login')
            type = request.Utilisateur.get('type')
            pass1 = request.Utilisateur.get('pass1')
            pass2  = request.Utilisateur.get('pass2')
            if pass1 == pass1:
                pass1 = pass1
            else:
                return  render(request, 'index.html', {'error_message':'Account Deactivaated'})



def save_user_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            #payss = Pays.objects.all()
            #data['html_pays_list'] = render_to_string('partials/pays/table_body.html', { 'data': payss })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)





def enregistrer(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
    else:
        form = UserForm()
    return save_user_form(request, form, 'login2.html')

class DashboardView(TemplateView):
    template_name = "dashboard.html"


def deconnexion(request):
    return render(request,'users/logout.html')