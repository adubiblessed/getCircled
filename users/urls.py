
from django.urls import path

from .views import login, register, home



urlpatterns = [
    #path('', login,  name='login'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
      
]