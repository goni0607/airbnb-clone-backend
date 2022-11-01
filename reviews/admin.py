from django.contrib import admin
from .models import Review


class GoodBadFilter(admin.SimpleListFilter):

    title = "Good or Bad!"

    parameter_name = "gb"

    def lookups(self, request, model_admin):
        return [
            ("good", "good>=3"),
            ("bad", "bad<3"),
        ]

    def queryset(self, request, reviews):
        status = self.value()
        if status == "good":
            return reviews.filter(rating__gte=3)
        elif status == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "room",
        "experience",
        "payload",
        "rating",
    )
    list_filter = (
        WordFilter,
        GoodBadFilter,
        "rating",
        "user__is_host",
    )
