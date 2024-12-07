from django.urls import path
from .views import AddReview, UserReviews, ReviewDetail, DeleteReview


urlpatterns = [
    path("add/", AddReview.as_view(), name="add_review"),
    path("", UserReviews.as_view(), name="reviews"),
    path("<slug:pk>/", ReviewDetail.as_view(), name="review_detail"),
    path("delete/<slug:pk>/", DeleteReview.as_view(), name="delete_review"),
]
