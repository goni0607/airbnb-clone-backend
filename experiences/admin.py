from django.contrib import admin
from .models import Experience, Perk
from categories import models as category_models


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
    list_filter = (
        "category",
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['category'].queryset = category_models.Category.objects.filter(
            kind=category_models.Category.CategoryKindChoices.EXPERIENCES)
        return form


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "description",
        "created_at",
    )
