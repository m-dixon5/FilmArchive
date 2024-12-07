from django.urls import path
from .views import Profile


urlpatterns = [
    path('user/<slug:pk>/', Profiles.as_view(), name="profile")
]