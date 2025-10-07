from django import forms

from .models import Eventdetails 

class EventForm(forms.ModelForm):
    class Meta:
        model = Eventdetails
        fields = ['event_name', 'event_date', 'event_time', 'event_location', 'event_description', 'event_image', 'capacity']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
        }