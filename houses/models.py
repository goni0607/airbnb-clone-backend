from django.db import models


class House(models.Model):

    """ Model definition for House """

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(help_text="Positive numbers only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Does this house allow pets?")

    def __str__(self) -> str:
        return self.name
