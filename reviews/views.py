from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.urls import reverse


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
        # Add the comment form and comments to the context
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(review=self.object)
        return context


class AddReview(LoginRequiredMixin, CreateView):
    """Add review view"""

    template_name = "reviews/add_review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Review added successfully!")
        return super(AddReview, self).form_valid(form)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit review"""

    template_name = "reviews/edit_review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/reviews/"

    def test_func(self):
        return self.request.user == self.get_object().user
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Review has been updated')
        return super().form_valid(form)
        

class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a review"""

    model = Review
    success_url = "/reviews/"

    def test_func(self):
        return self.request.user == self.get_object().user


class AddComment(LoginRequiredMixin, CreateView):
    """View to add a comment"""

    template_name = "reviews/review_detail.html"
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        # Set the review the comment belongs to
        review = Review.objects.get(pk=self.kwargs["pk"])
        form.instance.review = review
        form.instance.user = self.request.user
        messages.success(self.request, "Comment added successfully!")
        return super(AddComment, self).form_valid(form)

    def get_success_url(self):
        # Redirect back to the review detail page
        return reverse("review_detail", kwargs={"pk": self.kwargs["pk"]})


class DeleteComment(DeleteView):
    """View to delete a comment"""

    template_name = "reviews/delete_comment.html"
    model = Comment
    success_url = "/reviews/"

    def test_func(self):
        return self.request.user == self.get_object().name

    def delete(self, request):
        comment = self.get_object()
        comment.delete()
        messages.success(request, "Comment has been deleted.")
        return HttpResponseRedirect(self.success_url)
