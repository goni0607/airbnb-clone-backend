from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """ Room or Experience Category """

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20, choices=CategoryKindChoices.choices)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "categories"
