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
        return f"{self.user.username} on {self.platform}"
    
class UserQRCode(models.Model):
    user = models.OneToOneField('users.UserProfile', on_delete=models.CASCADE, related_name='qr_code')
    qr_code_image = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return f"QR Code for {self.user.username}"


class EventEnrollment(models.Model):
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='enrollments')
    event = models.ForeignKey('events.Eventdetails', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.event.event_name}"
    
class ChatMessage(models.Model):
    sender = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"