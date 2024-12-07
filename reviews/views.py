from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from .forms import ReviewForm


# Create your views here.
class UserReviews(ListView):
    """View all reviews"""

    template_name = "reviews/review.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetail(DetailView):
    """View individual reviews in more detail"""

    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"


class AddReview(LoginRequiredMixin, CreateView):
    """Add review view"""

    template_name = "reviews/add_review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a review"""
    model=Review
    success_url= '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user


