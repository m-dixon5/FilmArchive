from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Create your models here.
class Review(models.Model):
    """
    Model for creating reviews
    """
    user = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    summary = models.CharField(max_length=100)
    review = RichTextField(max_length=5000)
    film_image = ResizedImageField(
        size=(300, 450), quality=75, upload_to='reviews/', force_format='WEBP',
        blank=False, null=False
    )
    film_title = models.CharField(max_length=100, null=False, blank=False)
    film_rating = models.DecimalField(
        max_digits=3, decimal_places=1,
        validators=[MaxValueValidator(10.0), MinValueValidator(0.0)],  
        null=False, blank=False
    )
    date_watched = models.DateField()
    posted_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_on']
    
    def __str__(self):
        return str(self.title)

    def clean(self):
        super().clean()
        if self.film_rating > 10.0 or self.film_rating < 0.0:
            raise ValidationError({'Rating must be between 0 and 10'})