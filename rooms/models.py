from django.db import models
from common.models import CommonModel
from django.db.models import Sum


class Room(CommonModel):

    """ Room Model Definition """

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey("users.User",
                              related_name="rooms",
                              on_delete=models.CASCADE)
    amenities = models.ManyToManyField("rooms.Amenity",
                                       related_name="rooms")
    category = models.ForeignKey(
        "categories.Category",
        related_name="rooms",
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        return self.amenities.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return 0
        else:
            sum = self.reviews.aggregate(Sum("rating"))
            # total_rating = 0
            # for review in self.reviews.all().values("rating"):
            #     total_rating += review["rating"]
            return round(sum["rating__sum"] / count, 2)


class Amenity(CommonModel):

    """ Amenity Model Definition """

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
