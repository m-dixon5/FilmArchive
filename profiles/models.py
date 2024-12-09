from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField


# Create your models here.
class Profile(models.Model):
    """Profile model"""

    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="profiles/",
        force_format="WEBP",
        blank=False,
    )
    bio = RichTextField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)


class WatchLater(models.Model):
    """
    Model for adding films to watch later list
    """

    user = models.ForeignKey(
        User, related_name="review_author", on_delete=models.CASCADE
    )
    film_title = models.CharField(max_length=100, null=False, blank=False)
    film_image = ResizedImageField(
        size=(300, 450),
        quality=75,
        upload_to="reviews/",
        force_format="WEBP",
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.title)
