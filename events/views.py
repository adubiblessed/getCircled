from django.shortcuts import render, redirect

# Create your views here.

from .models import Eventdetails
from .forms import EventForm


def event_dashboard(request):
    eventlist = Eventdetails.objects.all()
    return render(request, 'events/dashboard.html',{'eventlist': eventlist})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user.organizerprofile
            event.save()
            form.save_m2m()
            return redirect('events:event_dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


def load_events(request):
    events = Eventdetails.objects.all()
    return render(request, 'partials/event_card.html', {'events': events})