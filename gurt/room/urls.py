from django.conf.urls import url
from django.urls import path
from .views import index, personal_room
from room import views
app_name = 'room'
urlpatterns = [
    path('', index, name='index'),
    path('<str:slug>/', personal_room, name='personal_room')
]