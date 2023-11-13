from django.contrib import admin
from .models import Rank, Servers, Requests, GameTypes

admin.site.register(Rank)
admin.site.register(Servers)
admin.site.register(Requests)
admin.site.register(GameTypes)


class RanksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position']

