from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date

import uuid


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique = True)
    phone_no = models.CharField(max_length = 10)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('organiser', 'Organiser')], default='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return "{}".format(self.email)
    

  

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=200, blank=True, null=True)
    user_image = models.ImageField(blank=True, null=True, upload_to='user_images/')
    created_at = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    # following = models.ManyToManyField(
    #     'self', 
    #     symmetrical=False, 
    #     related_name='followers', 
    #     blank=True
    # )


class EventOrganiserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizerprofile")
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    logo =  models.ImageField(upload_to='organizer_logos/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)


class UserConnection(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connection_sent")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connection_received")
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), 
                                                      ('accepted', 'Accepted'), 
                                                      ('rejected', 'Rejected')
                                                      ], default='pending')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Ensures that a user cannot send multiple connection requests to the same user
    class Meta:
        unique_together = ("sender", "reciever")
    

class EventFollow(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="followed_events")
    event = models.ForeignKey(EventOrganiserProfile, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")