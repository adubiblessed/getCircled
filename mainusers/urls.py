from django.urls import path



from .views import user_dashboard, profile_page, qr_code_view, event_details, load_anouncement


app_name = 'mainusers'

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/<str:username>', profile_page, name='profile_page'),
    path('qr_code/', qr_code_view, name='qr_code_view'),
    path('event/<int:event_id>/', event_details, name='event_details'),
    path('load/', load_anouncement, name='load_anouncement'),
]