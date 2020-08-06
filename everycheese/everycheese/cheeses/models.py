from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from model_utils.models import TimeStampedModel


class Cheese(TimeStampedModel):

    class Firmness(models.TextChoices):
        UNSPECIFIED = "non spécifié", "Non spécifié"
        SOFT = "pâte molle", "Pâte molle"
        SEMI_SOFT = "pâte demi-molle", "Pâte demi-molle"
        SEMI_HARD = "pâte demi-dure", "Pâte demi-dure"
        HARD = "pâte dure", "Pâte dure"

    name = models.CharField("nom du fromage", max_length=255)
    slug = AutoSlugField(
        "url du fromage",
        unique=True, always_update=False, populate_from="name",
    )
    firmness = models.CharField(
        "fermeté", max_length=20,
        choices=Firmness.choices, default=Firmness.UNSPECIFIED,
    )
    country_of_origin = CountryField(
        "Country of Origin", blank=True,
    )
    description = models.TextField("description", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'cheeses:detail',
            kwargs={'slug': self.slug},
        )
