from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .models import UserProfile, EventOrganiserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'user':
            UserProfile.objects.create(user=instance, username=instance.first_name_lower() + instance.last_name.lower())
            print ('user profile created')
        elif instance.role == 'organiser':
            EventOrganiserProfile.objects.create(user=instance, name=instance.first_name + ' ' + instance.last_name)
            print ('organiser profile created')
        