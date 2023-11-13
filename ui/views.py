from django.shortcuts import render
from rest_framework import viewsets
from .models import Rank, Servers, Requests, GameTypes
from .serializers import RankSerializer


# Create your views here.

def dashboard(request):
    return render(request, template_name='dashboard.jinja', )


def up_rank(request):
    return render(request, template_name='up_rank.jinja', )


def trading(request):
    return render(request, template_name='trading.jinja', )


class RanksViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
