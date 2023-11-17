from datetime import datetime

from django.db import models
import uuid


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    # server = models.ForeignKey('Server', on_delete=models.CASCADE)
    # current_rank = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='current_rank', null=True)
    # desired_rank = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='desired_rank', null=True)
    # employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    total = models.FloatField()
    status = models.CharField(max_length=200)
    stream_games = models.BooleanField(default=False)
    priority_order = models.BooleanField(default=False)
    desired_mastery = models.IntegerField()
    current_mastery = models.IntegerField()
    number_of_wins = models.IntegerField()
    number_of_games = models.IntegerField()
    ranked_genre = models.IntegerField()
    lp_Gain = models.IntegerField()
    current_lp = models.FloatField(max_length=99)
    request_recipient = models.DateTimeField(default=datetime.now())
    request_creation_date = models.DateTimeField(default=datetime.now())
    the_require_price = models.FloatField()
