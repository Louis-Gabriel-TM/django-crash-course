from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Cheese(TimeStampedModel):

    class Firmness(models.TextChoices):
        UNSPECIFIED = "non spécifié", "Non spécifié"
        SOFT = "pâte molle", "Pâte molle"
        SEMI_SOFT = "pâte demi-molle", "Pâte demi-molle"
        SEMI_HARD = "pâte demi-dure", "Pâte demi-dure"
        HARD = "pâte dure"

    name = models.CharField("nom du fromage", max_length=255)
    slug = AutoSlugField(
        "url du fromage",
        unique=True, always_update=False, populate_from="name",
    )
    description = models.TextField("description", blank=True)
    firmness = models.CharField(
        "fermeté", max_length=20,
        choices=Firmness.choices, default=Firmness.UNSPECIFIED,
    )

    def __str__(self):
        return self.name
