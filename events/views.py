from django.shortcuts import render, redirect

# Create your views here.

from .models import Eventdetails
from .forms import EventForm

def dashboard(request):
    eventlist = Eventdetails.objects.all()
    return render(request, 'events/dashboard.html')

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user.eventorganiserprofile
            event.save()
            form.save_m2m()
            return redirect('events:dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})