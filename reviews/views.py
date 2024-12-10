from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review, Comment
from .forms import ReviewForm, CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the comment form to the context
        context['form'] = CommentForm()
        return context


class AddReview(LoginRequiredMixin, CreateView):
    """Add review view"""

    template_name = "reviews/add_review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit review"""
    template_name= 'reviews/edit_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user



class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a review"""
    model=Review
    success_url= '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user


class AddComment(LoginRequiredMixin, CreateView):
    """View to add a comment"""
    template_name= 'reviews/review_detail.html'
    model = Comment
    form_class = CommentForm
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddComment, self).form_valid(form)


