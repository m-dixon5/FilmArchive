from django.urls import path
from .views import Profiles, EditProfile


urlpatterns = [
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("user/<slug:pk>/edit", EditProfile.as_view(), name="edit_profile"),
]