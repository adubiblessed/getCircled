from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Eventdetails, Anouncement
from .forms import EventForm


def event_dashboard(request):
    user = request.user
    eventlist = Eventdetails.objects.all()
    return render(request, 'events/dashboard.html',{'eventlist': eventlist, 'user': user})

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


# def load_events(request):
#     events = Eventdetails.objects.all()
#     return render(request, 'partials/event_card.html', {'events': events})


def event_details(request, event_id):
    event = get_object_or_404(Eventdetails, id=event_id)
    
    return render(request, 'events/event_details.html', {'event': event})

def make_announcement(request, event_id):
    event = get_object_or_404(Eventdetails, id=event_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        print(request.POST)
        if title and message:
            Anouncement.objects.create(event=event, title=title, message=message)
            return redirect('events:event_details', event_id=event.id)
    return render(request, 'events/make_announcement.html', {'event': event})