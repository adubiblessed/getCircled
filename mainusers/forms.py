from django import forms

from .models import UserSocialMedia

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = UserSocialMedia
        fields = ['platform', 'url']