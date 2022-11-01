from django.contrib import admin
from .models import Room, Amenity
from categories import models as category_models


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "price",
        # "^price", -- startswith
        # "=price", -- equal
        "owner__username",
    )
    list_filter = (
        "country",
        "city",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )

    # def total_amenities(self, room):
    #     return room.amenities.count()

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['category'].queryset = category_models.Category.objects.filter(
            kind=category_models.Category.CategoryKindChoices.ROOMS)
        return form


@ admin.register(Amenity)
class AemnityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
