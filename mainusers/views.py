from django.shortcuts import render

# Create your views here.


def user_dashboard(request):
    
    return render(request, 'mainusers/dashboard.html')

def profile_page(request):
    
    return render(request, 'mainusers/profile_page.html')