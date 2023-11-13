from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from .models import Rank, Server, Request, GameType

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = ['id','server','current_rank','desired_rank','details','total',
        'status','stream_games','priority_order','desired_mastery','current_mastery',
        'number_of_wins','number_of_games','ranked_genre','lp_Gain','current_lp',
        'request_recipient','request_creation_date','the_require_price']

class RankSerializer(ModelSerializer):
    class Meta:
        model = Rank
        fields = ['id','name','position']

class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = ['id','name','local']

class GameTypeSerializer(ModelSerializer):
    class Meta:
        model = GameType
        fields = ['id','release_date','name','publisher','developer','category']
        
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
