from django.db import models


class House(models.Model):

    """ Model definition for House """

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
