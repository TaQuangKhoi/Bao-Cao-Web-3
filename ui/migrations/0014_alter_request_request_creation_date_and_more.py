# Generated by Django 4.2.7 on 2023-11-17 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0013_alter_request_request_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 12, 51, 7, 131293)),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_recipient',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 12, 51, 7, 131293)),
        ),
    ]
