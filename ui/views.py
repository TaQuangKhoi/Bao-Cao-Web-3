from django.contrib.auth import logout
from django.http import HttpResponseRedirect
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
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, template_name='dashboard.jinja', )
    else:
        return HttpResponseRedirect('/signin/')


def trading(request):
    return render(request, template_name='trading.jinja', )


class RanksViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

