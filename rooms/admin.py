from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Amenity)
class AemnityAdmin(admin.ModelAdmin):
    pass
