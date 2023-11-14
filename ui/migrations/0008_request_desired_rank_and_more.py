# Generated by Django 4.2.7 on 2023-11-13 12:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0007_request_current_rank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='desired_rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desired_rank', to='ui.rank'),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 19, 12, 4, 938463)),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_recipient',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 19, 12, 4, 938463)),
        ),
    ]