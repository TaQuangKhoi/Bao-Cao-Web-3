import uuid
from django.contrib.auth.models import User

from django.db import models


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    server = models.ForeignKey('library_db.Server', on_delete=models.CASCADE, null=True)

    current_rank = models.ForeignKey('library_db.Rank', on_delete=models.CASCADE, related_name='current_rank',
                                     null=True)
    desired_rank = models.ForeignKey('library_db.Rank', on_delete=models.CASCADE, related_name='desired_rank',
                                     null=True)

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

    request_recipient = models.DateTimeField()
    request_creation_date = models.DateTimeField()

    the_require_price = models.FloatField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.details
