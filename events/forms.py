from django import forms


class EventForm(forms.Form):

    class Meta:
        fields = ["event_name", "event_date", "event_time", "event_location", "event_description", "event_image", "capacity"]