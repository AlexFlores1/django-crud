from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
def index(request):
    return render(request, 'index.html', {})

def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('todo')
            except:
                return render(request, 'signup.html', {'form':UserCreationForm, 'error':'el usuario ya existe'})
        else:
            return render(request, 'signup.html', {'form':UserCreationForm, 'error':'password no hacen match'})
    else:
        return render(request, 'signup.html', {'form':UserCreationForm})

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        context = {
            'form':AuthenticationForm()
        }
        return render(request, 'signin.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password =request.POST['password'])
        if user is None:
            context = {
            'form':AuthenticationForm(),
            'error':'Username or password is incorrect'
            }
            return render(request, 'signin.html', context)
        else:
            login(request, user)
            return redirect('index')