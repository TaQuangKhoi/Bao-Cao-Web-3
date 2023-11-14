from django.contrib import admin
from .models import (
    Rank,
    Server,
    Request,
    GameType
)


class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'server',
                    # 'current_rank',
                    # 'desired_rank',
                    'details', 'total',
                    'status', 'stream_games', 'priority_order', 'desired_mastery', 'current_mastery',
                    'number_of_wins', 'number_of_games', 'ranked_genre', 'lp_Gain', 'current_lp',
                    'request_recipient', 'request_creation_date', 'the_require_price']

    search_fields = ['server', 'current_rank', 'desired_rank', 'details', 'total',
                     'status', 'stream_games', 'priority_order', 'desired_mastery', 'current_mastery',
                     'number_of_wins', 'number_of_games', 'ranked_genre', 'lp_Gain', 'current_lp',
                     'request_recipient', 'request_creation_date', 'the_require_price']


class ServerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'local']
    search_fields = ['name', 'local']


class RankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position']
    search_fields = ['name', 'position']


class GameTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'release_date', 'name', 'publisher', 'developer', 'category']
    search_fields = ['release_date', 'name', 'publisher', 'developer', 'category']


admin.site.register(Request, RequestAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(GameType, GameTypeAdmin)
