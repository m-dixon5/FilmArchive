from django import forms
from .models import Profile
from djrichtextfield.widgets import RichTextWidget


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""

    class Meta:
        model = Profile
        fields = ["image", "bio"]

        labels = {"image": "Avatar", "bio": "Bio"}