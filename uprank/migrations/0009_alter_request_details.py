# Generated by Django 4.2.7 on 2023-11-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uprank', '0008_alter_request_lp_gain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='details',
            field=models.TextField(max_length=200, null=True),
        ),
    ]