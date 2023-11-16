from django.shortcuts import render


def up_rank(request):
    return render(request, template_name='up_rank.jinja', )