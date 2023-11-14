from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Rank,
    Server,
    Request,
    GameType
)
from .serializers import RankSerializer


def dashboard(request):
    return render(request, template_name='dashboard.jinja', )


def up_rank(request):
    return render(request, template_name='up_rank.jinja', )


def trading(request):
    return render(request, template_name='trading.jinja', )


class RanksViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
