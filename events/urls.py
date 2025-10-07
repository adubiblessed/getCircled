
from django.urls import path


from .views import event_dashboard, create_event, load_events

app_name = 'events'

urlpatterns = [
    path('dashboard/', event_dashboard, name='event_dashboard'),
    path('create_event/', create_event, name='create_event'),
    path('load/', load_events, name='load_events'),
]