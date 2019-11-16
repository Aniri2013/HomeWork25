from django.conf.urls import url
from .views import index
from student import views

app_name = 'student'
urlpatterns = [
    url('', index, name='index'),
]