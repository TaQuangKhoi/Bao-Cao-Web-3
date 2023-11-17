from django.shortcuts import render
from library_db.models import Rank


def up_rank(request):
    # get ranks with name distinct
    ranks = Rank.objects.values('name').distinct()
    rank_position = Rank.objects.values('position').distinct()
    print(rank_position)

    return render(
        request,
        template_name='up_rank.jinja',
        context={'ranks': ranks}
    )
