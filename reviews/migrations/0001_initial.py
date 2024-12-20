# Generated by Django 4.2.16 on 2024-12-03 11:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("summary", models.CharField(max_length=100)),
                ("review", djrichtextfield.models.RichTextField(max_length=5000)),
                (
                    "film_image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=(300, 450),
                        upload_to="reviews/",
                    ),
                ),
                ("film_title", models.CharField(max_length=100)),
                (
                    "film_rating",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=3,
                        validators=[django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                ("date_watched", models.DateField()),
                ("posted_on", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-posted_on"],
            },
        ),
    ]
