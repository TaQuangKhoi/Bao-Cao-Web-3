import uuid

from django.db import models


class Rank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)


class Server(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    local = models.CharField(max_length=50)


class GameType(models.Model):
    id = models.AutoField(primary_key=True)
    release_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
