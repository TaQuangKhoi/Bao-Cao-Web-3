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
    Status = models.OneToOneField('Status', on_delete=models.CASCADE)
    Select_Champion = models.OneToOneField('Champions', on_delete=models.CASCADE)
    Stream_Games = models.OneToOneField('GameTypes', on_delete=models.CASCADE)
    Priority_Order = models.OneToOneField('Priority', on_delete=models.CASCADE)
    Desired_Mastery = models.OneToOneField('Mastery', on_delete=models.CASCADE)
    Current_Mastery = models.OneToOneField('Mastery', on_delete=models.CASCADE)
    Number_of_Wins = models.OneToOneField('Wins', on_delete=models.CASCADE)
    Number_of_Games = models.OneToOneField('Games', on_delete=models.CASCADE)
    Ranked_Genre = models.OneToOneField('RankedGenre', on_delete=models.CASCADE)
    Select_Server = models.OneToOneField('Servers', on_delete=models.CASCADE)
    Desired_Rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
    Select_LP_Gain = models.OneToOneField('LP', on_delete=models.CASCADE)
    Select_Current_LP = models.OneToOneField('LP', on_delete=models.CASCADE)
    Current_Rank = models.OneToOneField('Ranks', on_delete=models.CASCADE)
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