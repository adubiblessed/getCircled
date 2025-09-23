from django.contrib import admin

# Register your models here.

from .models import User, UserProfile, EventOrganiserProfile, UserConnection, EventFollow

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(EventOrganiserProfile)
admin.site.register(UserConnection)
admin.site.register(EventFollow)
