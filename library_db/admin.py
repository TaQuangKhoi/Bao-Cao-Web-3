from django.contrib import admin
from .models import (
    Rank,
    Server,
    GameType,
)


class ServerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'local']
    search_fields = ['name', 'local']


class RankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position']
    search_fields = ['name', 'position']


class GameTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'release_date', 'name', 'publisher', 'developer', 'category']
    search_fields = ['release_date', 'name', 'publisher', 'developer', 'category']


admin.site.register(Rank, RankAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(GameType, GameTypeAdmin)
