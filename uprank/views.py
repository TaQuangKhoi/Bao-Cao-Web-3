from django.shortcuts import render
from library_db.models import Rank
from uprank.forms import UpRankForm


def up_rank(request):
    form = UpRankForm()
    current_ranks = Rank.objects.values('name').distinct()
    rank_positions = Rank.objects.values('position').distinct()

    return render(
        request,
        template_name='up_rank.jinja',
        context={
            'form': form,
            'current_ranks': current_ranks,
            'rank_positions': rank_positions,
        }
    )
