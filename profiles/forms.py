from django import forms
from .models import Profile, WatchLater
from djrichtextfield.widgets import RichTextWidget


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""

    class Meta:
        model = Profile
        fields = ["image", "bio"]

        labels = {"image": "Avatar", "bio": "Bio"}


class WatcherLaterForm(forms.ModelForm):
    """Form to add a film to watch later list"""

    class Meta:
        model = WatchLater
        fields = [
            "film_title",
            "film_image",
        ]

        review = forms.CharField(widget=RichTextWidget())

        labels = {
            "film_title": "Film Title",
            "film_image": "Film Image",
        }
