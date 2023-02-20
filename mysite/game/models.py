from django.db import models
from user.models import User
from home.models import Group

# Create your models here.

class Game(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    max_points = models.IntegerField()
    keeper_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hosting_group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

class Task(models.Model):
    TASK_TYPES = (("L", "Go to location"),
                  ("R", "Pick up litter"))
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    task_number = models.IntegerField()
    task_type = models.CharField(max_length=1, choices=TASK_TYPES)
    points = models.IntegerField()

    class Meta:
        unique_together = ("game_id", "task_number")

class Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "game_id")

class Completion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    task_number = models.ForeignKey(Task, on_delete=models.CASCADE)
    #fields here for submission content

    class Meta:
        unique_together = ("user_id", "game_id", "task_number")
