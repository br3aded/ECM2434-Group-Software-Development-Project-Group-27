# Generated by Django 4.1.5 on 2023-03-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_alter_submission_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
