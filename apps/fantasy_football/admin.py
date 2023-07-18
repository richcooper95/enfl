from django.contrib import admin

from .models import FantasyFootballSeason


# Register your models here.
class FantasyFootballSeasonAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(FantasyFootballSeason, FantasyFootballSeasonAdmin)
