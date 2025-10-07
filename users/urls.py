
from django.urls import path

from .views import login, register, home

app_name = 'users'

urlpatterns = [
    #path('', login,  name='login'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
      
]