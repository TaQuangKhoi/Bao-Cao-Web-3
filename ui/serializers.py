from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from .models import Rank, Servers, Requests, GameTypes


class RankSerializer(ModelSerializer):
    class Meta:
        model = Rank
        fields = ['id', 'name', 'position']

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
