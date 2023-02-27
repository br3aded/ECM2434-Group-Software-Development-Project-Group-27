# Generated by Django 4.1.5 on 2023-02-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_completions_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_uri', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Playing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_position', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='completions',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='completions',
            name='game_id',
        ),
        migrations.RemoveField(
            model_name='completions',
            name='task_number',
        ),
        migrations.RemoveField(
            model_name='completions',
            name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='players',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='players',
            name='game_id',
        ),
        migrations.RemoveField(
            model_name='players',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='max_points',
            new_name='points',
        ),
        migrations.AddField(
            model_name='game',
            name='game_state',
            field=models.CharField(choices=[('W', 'Waiting'), ('R', 'In Progress'), ('J', 'Judging'), ('F', 'Finished')], default='W', max_length=1),
        ),
    ]