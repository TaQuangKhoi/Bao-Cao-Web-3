# Generated by Django 4.2.7 on 2023-11-17 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0008_request_desired_rank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 12, 41, 27, 798178)),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_recipient',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 12, 41, 27, 797184)),
        ),
    ]
