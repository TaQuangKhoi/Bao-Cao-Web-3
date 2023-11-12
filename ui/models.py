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
    champion = models.OneToOneField('Champions', on_delete=models.CASCADE)
    stream_games = models.BooleanField(default=False)
    priority_order = models.BooleanField(default=False)
    desired_mastery = models.IntegerField( max_length=7)
    current_mastery = models.IntegerField( max_length=6)
    number_of_wins = models.IntegerField( max_length=99)
    number_of_games = models.IntegerField( max_length=99)
    ranked_genre = models.IntegerField( max_length=2)
    desired_rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    lp_Gain = models.IntegerField( max_length= 35)
    current_lp = models.FloatField( max_length=99)
    current_rank = models.FloatField( max_length=99)
    request_recipient = models.OneToOneField('RequestRecipient', on_delete=models.CASCADE)
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
    release_date = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)