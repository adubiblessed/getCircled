from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls'), name='home'),
    path('events/', include('events.urls'), name="events")
]
  