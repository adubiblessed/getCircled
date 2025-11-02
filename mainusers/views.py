from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
from users.models import UserProfile, UserConnection
from events.models import Eventdetails
from .models import EventEnrollment

def user_dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    return render(request, 
                    'mainusers/dashboard.html', 
                    {'profile': profile,})

def load_dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    # Get all pending requests where the current user is the receiver
    pending_requests = UserConnection.objects.filter(
        reciever=request.user,
        status='pending'
    )

    events = Eventdetails.objects.all()
    enrolled_events = Eventdetails.objects.filter(enrollments__user=profile)

    announcements = []
    for event in enrolled_events:
        announcements.extend(event.announcements.all())
    announcements.sort(key=lambda x: x.created_at, reverse=True)
    # print(announcements)
    # print(enrolled_events)
    
    return render(request, 
                    'mainusers/partials/dashboard.html', 
                    {'profile': profile, 
                    'announcements': announcements, 
                    'events': enrolled_events, 
                    'pending_requests': pending_requests})

def profile_page_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'mainusers/profile_page.html', {'profile': profile})

@login_required(login_url='/login/')
def profile_page(request, username):
    profile = get_object_or_404(UserProfile, username=username)

    # Prevent connecting to self
    if profile.user == request.user:
        return render(request, 'mainusers/profile_page.html', {'profile': profile})

    # Check if a POST request (user clicked the connect button)
    if request.method == "POST":
        connection, created = UserConnection.objects.get_or_create(
            sender=request.user,
            reciever=profile.user  
        )

        if not created:
            messages.info(request, "You have already sent a connection request to this user.")
        else:
            messages.success(request, "Connection request sent successfully!")

        return redirect('mainusers:profile_page', username=username)

    # Get connection status (to show correct button)
    connection_status = "none"
    try:
        conn = UserConnection.objects.get(sender=request.user, reciever=profile.user)
        connection_status = conn.status
    except UserConnection.DoesNotExist:
        try:
            reverse_conn = UserConnection.objects.get(sender=profile.user, reciever=request.user)
            connection_status = reverse_conn.status
        except UserConnection.DoesNotExist:
            pass

    return render(request, 'mainusers/profile_page.html', {
        'profile': profile,
        'connection_status': connection_status,
    })

# def load_connection(request):
#     # Get all pending requests where the current user is the receiver
#     pending_requests = UserConnection.objects.filter(
#         reciever=request.user,
#         status='pending'
#     )

#     return render(request, 'mainusers/partials/connection.html', {
#         'pending_requests': pending_requests
#     })

def respond_to_connection(request, connection_id, action):
    connection = get_object_or_404(UserConnection, id=connection_id)

    # Ensure only the receiver can respond
    if connection.reciever != request.user:
        messages.error(request, "You are not authorized to respond to this request.")
        return redirect('connection_requests')

    if action == 'accept':
        connection.status = 'accepted'
        connection.is_accepted = True
        connection.save()
        messages.success(request, f"You are now connected with {connection.sender.username}!")

    elif action == 'reject':
        connection.status = 'rejected'
        connection.is_accepted = False
        connection.save()
        messages.info(request, f"You rejected {connection.sender.username}'s connection request.")

    return redirect('mainusers:user_dashboard')

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
        return redirect('mainusers:event_list')
        

    return render(request, 'mainusers/event_details.html', {'event': event, 'is_enrolled':is_enrolled})


def event_list(request):
    event = Eventdetails.objects.all()
    return render(request, 'mainusers/events_list.html', {'events': event})

# def load_anouncement(request):
#     profile = get_object_or_404(UserProfile, user=request.user)
    
#     return render(request, 'mainusers/partials/annoucement.html', {'announcement': announcements})

# def load_event(request):
#     profile = get_object_or_404(UserProfile, user=request.user)
#     enrolled_events = Eventdetails.objects.filter(enrollments__user=profile)
#     return render(request, 'mainusers/partials/event_card.html', {'events': enrolled_events})