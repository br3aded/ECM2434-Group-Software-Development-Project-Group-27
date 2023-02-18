# Generated by Django 4.1.5 on 2023-02-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_purchases_unique_together'),
        ('game', '0002_game_hosting_group_task_players_completions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='completions',
            unique_together={('user_id', 'game_id', 'task_number')},
        ),
        migrations.AlterUniqueTogether(
            name='players',
            unique_together={('user_id', 'game_id')},
        ),
    ]
