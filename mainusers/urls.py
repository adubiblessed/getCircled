from django.urls import path



from .views import user_dashboard


app_name = 'mainusers'

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/{user_name}', profile_page, name='profile_page'),
]