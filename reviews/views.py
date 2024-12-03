from django.views.generic import CreateView

from .models import Review
from .forms import ReviewForm

# Create your views here.
class AddReview(CreateView):
    """ Add review view """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)
