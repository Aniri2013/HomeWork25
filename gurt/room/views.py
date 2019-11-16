from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Room
from django import forms

def index(request):
    print()
    room = Room.objects.all()
    print(room)
    print()
    return render(request, "room/room.html", context={"room": room})

def personal_room (request, slug):
    room = Room.objects.get(slug=slug)
    print()
    print('personal room')
    print()
    return render(request, 'room/personal_room.html', context={'room': room})
