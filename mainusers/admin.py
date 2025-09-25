from django.contrib import admin

# Register your models here.
from .models import UserQRCode, UserSocialMedia, EventEnrollment

admin.site.register(UserSocialMedia)
admin.site.register(UserQRCode)
admin.site.register(EventEnrollment)

