from django.db import models


# Create your models here.


class Eventdetails(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=200)
    event_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organiser = models.ForeignKey('users.EventOrganiserProfile', on_delete=models.CASCADE, related_name='events')
    attendees = models.ManyToManyField('users.UserProfile', related_name='attended_events', blank=True)
    event_image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    event_qr_code = models.ImageField(upload_to='event_qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.event_name} by {self.organiser.name}id {self.id} "


class Anouncement(models.Model):
    event = models.ForeignKey(Eventdetails, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement for {self.event.event_name}: {self.title}"
    

