# Generated by Django 4.1.5 on 2023-02-26 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_remove_game_end_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='points',
        ),
    ]
