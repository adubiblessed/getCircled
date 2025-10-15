from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import Eventdetails
from users.utils import generate_qr_code
from config.settings import BASE_URL


@receiver(post_save, sender=Eventdetails)
def event_qr_code_gen(sender, instance, created, **kwargs):
    if created and not instance.event_qr_code:
        event_id = instance.id
        data = f"{BASE_URL}events/{event_id}/"
        file_path  = generate_qr_code(data, f"{event_id}_qr.png", logo_path=None)

        Eventdetails.objects.filter(id=event_id).update(event_qr_code=file_path)