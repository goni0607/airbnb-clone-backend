from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    file = models.URLField()
    description = models.CharField(max_length=150,)
    room = models.ForeignKey(
        "rooms.Room",
        related_name="photos",
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    experience = models.ForeignKey(
        "experiences.Experience",
        related_name="photos",
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def __str__(self) -> str:
        return "Photo File"


class Video(CommonModel):

    file = models.URLField()
    experience = models.OneToOneField(
        "experiences.Experience",
        related_name="vodeo",
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def __str__(self) -> str:
        return "Video File"
