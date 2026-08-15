from django.contrib import admin
from .models import Trail, Park


@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = ("name", "region")


@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "park",
        "distance_km",
        "elevation_gain",
        "difficulty",
        "is_open",
    )
    list_filter = ("park", "difficulty", "is_open")
    search_fields = ("name",)