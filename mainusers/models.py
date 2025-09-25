from django.db import models

# Create your models here.

SOCIAL_MEDIA_CHOICES = [
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('linkedin', 'LinkedIn'),
    ('instagram', 'Instagram'),
    ('github', 'GitHub'),
    ('website', 'Website'),
    ('youtube', 'YouTube'),
    ('tiktok', 'TikTok'),
    ('whatsapp', 'WhatsApp'),
]

class UserSocialMedia(models.Model):
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='social_media')
    platform = models.CharField(choices=SOCIAL_MEDIA_CHOICES, max_length=20)
    profile_url = models.URLField()

    def __str__(self):
        return f"{self.user.name} on {self.platform}"
    
class UserQRCode(models.Model):
    user = models.OneToOneField('users.UserProfile', on_delete=models.CASCADE, related_name='qr_code')
    qr_code_image = models.ImageField(upload_to='user_qr_codes/')

    def __str__(self):
        return f"QR Code for {self.user.name}"


class EventEnrollment(models.Model):
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='enrollments')
    event = models.ForeignKey('events.Eventdetails', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} enrolled in {self.event.event_name}"
    
