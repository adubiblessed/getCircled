from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.
from users.models import UserProfile
from events.models import Eventdetails
from .models import EventEnrollment

def user_dashboard(request):
    
    return render(request, 'mainusers/dashboard.html')

def profile_page(request, username):
    profile = get_object_or_404(UserProfile, username=username)
    return render(request, 'mainusers/profile_page.html', {'profile': profile})

def qr_code_view(request):
    #get current user username
    profile = get_object_or_404(UserProfile, user=request.user)
    qr_code = profile.qr_code.qr_code_image.url if hasattr(profile, 'qr_code') else None
    return render(request, 'mainusers/qr_code.html', {'profile': profile, 'qr_code': qr_code})

def event_details(request, event_id):
    event = get_object_or_404(Eventdetails, id=event_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    # enroll for event
    is_enrolled = event.enrollments.filter(user=profile).exists()
    if request.method == 'POST' and not is_enrolled:
        EventEnrollment.objects.create(user=profile, event=event)
        

    return render(request, 'mainusers/event_details.html', {'event': event, 'is_enrolled':is_enrolled})

def load_anouncement(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    enrolled_events = Eventdetails.objects.filter(enrollments__user=profile)
    announcements = []
    for event in enrolled_events:
        announcements.extend(event.announcements.all())
    announcements.sort(key=lambda x: x.created_at, reverse=True)
    return render(request, 'mainusers/partials/annoucement.html', {'announcement': announcements})
