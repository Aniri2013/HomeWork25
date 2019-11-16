from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def RegView(request):
    form = UserCreationForm(request.POST)
    return render(request, 'newmodule/reg.html', context={'form': form})


def RegCreate(request):
    print()
    print('Привет!!!')
    print()
    if request.method == 'POST':
        print()
        print('Привет!!!')
        print()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print()
            print('Form valid')
            print()
            user = form.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000/login/')
    else:
        return HttpResponseRedirect('/register/')


def LogView(request):
    form = AuthenticationForm()
    return render(request, 'newmodule/log.html', context={'form': form})

def LogEnter(request):
    print()
    print('Hello!!!')
    print()
    if request.method == 'POST':
        print()
        print('Hiiii!!!')
        print()
        username = request.POST.get('username')
        password = request.POST.get('password')
        print()
        print('username = ', username)
        print('password = ', password)
        print()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/room/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')

def HomeView(request):
    return render(request, 'newmodule/room.html')

def LogoutView(request):
    print()
    print('Hello!!!')
    print()
    if request.method == 'POST':
        print()
        print('Hiiii!!!')
        print()
        logout(request)
        return redirect('http://127.0.0.1:8000/login/')
    else:
        return redirect('http://127.0.0.1:8000/home/')