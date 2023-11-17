from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Rank,
    Server,
    Request,
    GameType
)
from .serializers import RankSerializer


def trading(request):
    return render(request, template_name='trading.jinja', )


class RanksViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


