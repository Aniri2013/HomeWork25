from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from newmodule.views import *
from room.views import *
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'student/', include('student.urls')),
    path(r'room/', include('room.urls')),
    path('register/', RegView),
    path('register/create', RegCreate, name='register'),
    path('login/', LogView),
    path('login/enter', LogEnter, name='login'),
    path('home/', HomeView, name='home'),
    path('logout', LogoutView, name='logout'),
]
