from django.db import models

# Create your models here.
class Requests(models.Model):
    id = models.AutoField(primary_key=True)
    server = models.OneToOneField('Servers', on_delete=models.CASCADE)
    current_rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    desired_rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    Employee = models.OneToOneField('Employees', on_delete=models.CASCADE)
    Details = models.OneToOneField('Details', on_delete=models.CASCADE)
    Total = models.OneToOneField('Total', on_delete=models.CASCADE)
    Status = models.CharField(max_length=200)
    Select_Champion = models.OneToOneField('Champions', on_delete=models.CASCADE)
    Stream_Games = models.BooleanField(default=False)
    Priority_Order = models.BooleanField(default=False)
    Desired_Mastery = models.IntegerField( max_length=7)
    Current_Mastery = models.IntegerField( max_length=6)
    Number_of_Wins = models.FloatField( max_length=50)
    Number_of_Games = models.FloatField( max_length=50)
    Ranked_Genre = models.IntegerField( max_length=2)
    Desired_Rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    Select_LP_Gain = models.IntegerField( max_length= 35)
    Select_Current_LP = models.FloatField( max_length=99)
    Current_Rank = models.FloatField( max_length=99)
    Petitioner = models.OneToOneField('Petitioner', on_delete=models.CASCADE)
    Request_recipient = models.OneToOneField('RequestRecipient', on_delete=models.CASCADE)
    Request_creation_date = models.OneToOneField('RequestCreationDate', on_delete=models.CASCADE)
    The_require_price = models.OneToOneField('TheRequirePrice', on_delete=models.CASCADE) 


class Ranks(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)

class Servers(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Local = models.CharField(max_length=50)

class GameTypes(models.Model):
    id = models.AutoField(primary_key=True)
    Release_date = models.CharField(max_length=50)
    Game_Name = models.CharField(max_length=50)
    Publisher = models.CharField(max_length=50)
    Developer = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)