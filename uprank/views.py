from django.shortcuts import render
from library_db.models import Rank
from uprank.forms import UpRankForm
from uprank.models import Request


def up_rank(request):
    form = UpRankForm()

    if request.method == "POST":
        form = UpRankForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            new_current_rank = Rank.objects.get(name=cleaned_data['current_rank'],
                                                position=cleaned_data['current_rank_position'])
            print(new_current_rank)
            new_request = Request(

            )
            # new_request.save()
        else:
            print('The form was invalid.')
            print(form.errors)

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
