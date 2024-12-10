from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    """Form to create a Review"""

    class Meta:
        model = Review
        fields = [
            "film_title",
            "film_image",
            "film_rating",
            "summary",
            "review",
            "date_watched",
        ]

        review = forms.CharField(widget=RichTextWidget())

        widget = {
            "summary": forms.Textarea(attrs={"rows": 3}),
        }

        labels = {
            "film_title": "Film Title",
            "film_image": "Film Image",
            "film_rating": "Rating",
            "summary": "Review Summary",
            "review": "Review",
            "date_watched": "Date Watched",
        }


class CommentForm(forms.ModelForm):
    """ Form to create a Comment """

    class Meta:
        model = Comment
        fields = ["body",]

        labels = {"body": "Body"}