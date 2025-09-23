from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required= True,
        label = "Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    is_organiser = forms.BooleanField(
        required=False,
        label="Register as organiser",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_no", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'] 
        user.username = self.cleaned_data['email'] 
        user.role = "organiser" if self.cleaned_data.get("is_organiser") else "user"
        
        if commit:
            user.save()
        return user




class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("email", "password")