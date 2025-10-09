from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from users.models import UserProfile

def user_dashboard(request):
    
    return render(request, 'mainusers/dashboard.html')

def profile_page(request, username):
    profile = get_object_or_404(UserProfile, username=username)
    return render(request, 'mainusers/profile_page.html', {'profile': profile})
