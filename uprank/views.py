from django.shortcuts import render
from library_db.models import Rank


def up_rank(request):
    # get ranks with name distinct
    ranks = Rank.objects.values('name').distinct()
    rank_positions = Rank.objects.values('position').distinct()

    return render(
        request,
        template_name='up_rank.jinja',
        context={
            'ranks': ranks,
            'rank_positions': rank_positions,
        }
    )
