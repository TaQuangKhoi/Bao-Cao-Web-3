from django.db import models

# Create your models here.
class Requests(models.Model):
    id = models.AutoField(primary_key=True)
    server = models.OneToOneField('Servers', on_delete=models.CASCADE)
    current_rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    desired_rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    employee = models.OneToOneField('Employees', on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    total = models.FloatField()
    status = models.CharField(max_length=200)
    stream_games = models.BooleanField(default=False)
    priority_order = models.BooleanField(default=False)
    desired_mastery = models.IntegerField()
    current_mastery = models.IntegerField()
    number_of_wins = models.IntegerField()
    number_of_games = models.IntegerField()
    ranked_genre = models.IntegerField( )
    lp_Gain = models.IntegerField()
    current_lp = models.FloatField( max_length=99)
    request_recipient = models.DateTimeField(auto_now_add=True)
    request_creation_date = models.DateTimeField(auto_now_add=True)
    the_require_price = models.FloatField()   

class Ranks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

class Servers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    local = models.CharField(max_length=50)

class GameTypes(models.Model):
    id = models.AutoField(primary_key=True)
    release_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)