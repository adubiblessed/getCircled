import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .models import UserProfile, EventOrganiserProfile
from mainusers.models import UserQRCode

from .utils import generate_qr_code

BASE_URL = "http://127.0.0.1:8000/"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:

        return
    if instance.role == 'user':
        profile = UserProfile.objects.create(
            user=instance, 
            username=instance.first_name.lower() + instance.last_name.lower()
            #if username already exists, use the fisrt part of email before @ as username
            if UserProfile.objects.filter(username=instance.first_name.lower() + instance.last_name.lower()).exists()
            else instance.email.split('@')[0]
            )
        data = f"{BASE_URL}profile/{profile.username}"
        file_path  = f"{profile.username}_qr.png"
        generate_qr_code(data, file_path)
        UserQRCode.objects.create(user=profile, qr_code_image=file_path)
        print ('user profile created')
    elif instance.role == 'organiser':
        EventOrganiserProfile.objects.create(user=instance, name=instance.first_name + ' ' + instance.last_name)
        print ('organiser profile created')
        