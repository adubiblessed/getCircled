from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls',namespace='user'), name='user'),
    path('', include('mainusers.urls',namespace='mainusers'), name='mainusers'),
    path('e/', include('events.urls'), name="events")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  