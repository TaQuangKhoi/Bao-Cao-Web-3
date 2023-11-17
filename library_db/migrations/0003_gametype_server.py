# Generated by Django 4.2.7 on 2023-11-17 05:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library_db', '0002_delete_gametype_delete_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=50)),
            ],
        ),
    ]
