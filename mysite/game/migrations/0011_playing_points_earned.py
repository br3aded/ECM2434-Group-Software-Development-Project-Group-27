# Generated by Django 4.1.5 on 2023-03-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_remove_playing_active_task_game_active_task_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playing',
            name='points_earned',
            field=models.IntegerField(default=0),
        ),
    ]