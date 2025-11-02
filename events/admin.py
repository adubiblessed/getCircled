from django.contrib import admin

# Register your models here.
from .models import Eventdetails, Anouncement


admin.site.register(Eventdetails)
admin.site.register(Anouncement)