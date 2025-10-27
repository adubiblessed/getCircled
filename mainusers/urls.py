from django.urls import path



from .views import (user_dashboard, 
                    profile_page_view, 
                    profile_page,
                    qr_code_view, 
                    event_details,
                    load_dashboard, 
                    respond_to_connection,
                    # load_anouncement,
                    # load_connection,
                    # load_event
                    event_list
                    )


app_name = 'mainusers'

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile', profile_page_view, name='profile_page'),
    path('profile/<str:username>', profile_page, name='profile_page'),
    path('qr_code/', qr_code_view, name='qr_code_view'),
    path('event/<int:event_id>/', event_details, name='event_details'),
    path('load_dashboard/', load_dashboard, name='load_dashboard'),
    
    path('connections/<int:connection_id>/<str:action>/', respond_to_connection, name='respond_to_connection'),
    path('event_list/', event_list, name='event_list'),
]