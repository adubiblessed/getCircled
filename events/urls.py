
from django.urls import path


from .views import event_dashboard, create_event, event_details, make_announcement

app_name = 'events'

urlpatterns = [
    path('dashboard/', event_dashboard, name='event_dashboard'),
    path('create_event/', create_event, name='create_event'),
    #path('load/', load_events, name='load_events'),

    path('details/<int:event_id>/', event_details, name='event_details'),
    path('details/<int:event_id>/announce/', make_announcement, name='make_announcement'),
]