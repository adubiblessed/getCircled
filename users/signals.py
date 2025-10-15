import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
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
        base_username = ((instance.first_name + instance.last_name).lower() 
                         if instance.first_name and instance.last_name else instance.email.split('@')[0])

        # Check for duplicates
        if UserProfile.objects.filter(username=base_username).exists():
            base_username = instance.email.split('@')[0]

        # Create the user profile
        profile = UserProfile.objects.create(
            user=instance,
            username=base_username
        )

        logo_path = os.path.join(settings.BASE_DIR, 'media', 'qr_codes', 'getcircledlogo.png')

        data = f"{BASE_URL}profile/{profile.username}"
        file_path  = generate_qr_code(data, f"{profile.username}_qr.png", logo_path=logo_path)
        
        UserQRCode.objects.create(user=profile, qr_code_image=file_path)
        print ('user profile created')
    elif instance.role == 'organiser':
        EventOrganiserProfile.objects.create(user=instance, name=instance.first_name + ' ' + instance.last_name)
        print ('organiser profile created')
        