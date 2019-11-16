from django.urls import path, include
from .views import *

urlpatterns = [
path('', RegView.as_view()),
path('', RegView),
]