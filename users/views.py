from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import RegisterForm, LoginForm
from django.db import IntegrityError

# Create your views here.

#temporary home view
def home(request):
    User = request.user
    if not User.is_authenticated:
        return redirect('users:login')
    if User.role == "user":
        return redirect('mainusers:user_dashboard')
    elif User.role == "organiser":
        return redirect('event_dashboard')

    return render(request, 'users/home.html', {'user': User})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            auth_login(request, form.get_user())
            return redirect('users:home')  
        
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            try:
                user = form.save()
                print(f"User created successfully: {user.email}")
                return redirect('users:login')
            except IntegrityError as e:
                print(f"Database error: {e}")
                form.add_error('email', 'A user with this email already exists.')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})



