from django.urls import path
from .views import AddReview, UserReviews


urlpatterns = [
    path("", AddReview.as_view(), name="add_review"),
    path("reviews/", UserReviews.as_view(), name="reviews"),
]
