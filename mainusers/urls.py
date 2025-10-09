from django.urls import path



from .views import user_dashboard, profile_page


app_name = 'mainusers'

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/<str:username>', profile_page, name='profile_page'),
]