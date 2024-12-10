from django.contrib import admin
from .models import Review, Comment


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "film_title", "summary", "review", "posted_on")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "review", "body", "created_on")
