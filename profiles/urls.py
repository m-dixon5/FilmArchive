from django.urls import path
from .views import Profiles, EditProfile, WatchLaterAdd


urlpatterns = [
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("user/<slug:pk>/edit", EditProfile.as_view(), name="edit_profile"),
    path("user/<slug:pk>/watchlater", WatchLaterAdd.as_view(),
         name="add_watchlater"),
]