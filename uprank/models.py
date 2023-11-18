import uuid
from django.contrib.auth.models import User

from django.db import models


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    current_rank = models.ForeignKey('library_db.Rank', on_delete=models.CASCADE, related_name='current_rank',
                                     null=True)
    current_lp = models.FloatField(max_length=99, null=True)
    lp_Gain = models.IntegerField()

    desired_rank = models.ForeignKey('library_db.Rank', on_delete=models.CASCADE,
                                     related_name='desired_rank',
                                     null=True)
    server = models.ForeignKey('library_db.Server', on_delete=models.CASCADE, null=True)

    details = models.CharField(max_length=200, null=True)
    total = models.FloatField()
    status = models.CharField(max_length=200, null=True)

    priority_order = models.BooleanField(default=False)
    stream_games = models.BooleanField(default=False)

    desired_mastery = models.IntegerField(null=True)
    current_mastery = models.IntegerField(null=True)

    number_of_wins = models.IntegerField(null=True)
    number_of_games = models.IntegerField(null=True)

    ranked_genre = models.IntegerField(null=True)

    request_recipient = models.DateTimeField(null=True)
    request_creation_date = models.DateTimeField(null=True)

    the_require_price = models.FloatField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.details
