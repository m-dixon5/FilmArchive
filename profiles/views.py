from django.views.generic import TemplateView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Profile, WatchLater
from .forms import ProfileForm, WatcherLaterForm
from django.contrib import messages


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {"profile": profile, "form": ProfileForm(instance=profile)}

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""

    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.success_url = f"/profiles/user/{self.object.user.id}"
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class WatchLaterAdd(LoginRequiredMixin, CreateView):
    """Add watch list item"""

    template_name = "profiles/watch_Later.html"
    model = WatchLater
    form_class = WatcherLaterForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Added film to Watch Later")
        return super(WatchLaterAdd, self).form_valid(form)