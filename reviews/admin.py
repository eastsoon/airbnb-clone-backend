from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by star!"
    parameter_name = "result"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good (star 5 ~ 3)"),
            ("bad", "Bad (star 0 ~ 2)"),
        ]

    def queryset(self, request, reviews):
        result = self.value()
        if result == "good":
            return reviews.filter(rating__gt=2)
        elif result == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
    )
