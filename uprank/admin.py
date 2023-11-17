from django.contrib import admin
from .models import (
    Request,
)
# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id',
                    # 'server',
                    # 'current_rank',
                    # 'desired_rank',
                    'details', 'total',
                    'status', 'stream_games', 'priority_order', 'desired_mastery', 'current_mastery',
                    'number_of_wins', 'number_of_games', 'ranked_genre', 'lp_Gain', 'current_lp',
                    'request_recipient', 'request_creation_date', 'the_require_price']

    search_fields = [
        # 'server', 'current_rank', 'desired_rank',
        'details', 'total',
        'status', 'stream_games', 'priority_order', 'desired_mastery', 'current_mastery',
        'number_of_wins', 'number_of_games', 'ranked_genre', 'lp_Gain', 'current_lp',
        'request_recipient', 'request_creation_date', 'the_require_price'
    ]


admin.site.register(Request, RequestAdmin)
