from django.contrib import admin
from .models import Experience, Perk


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "host",
        "price",
        "start_time",
        "end_time",
        "created_at",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "description",
        "created_at",
    )
