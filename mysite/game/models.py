from django.db import models
from user.models import AppUser
from home.models import Group

#Note for all ManyToMany relations, the django M2M field is stored in
#what would be the destination side of the arrow in the ER diagram

#TODO:
#Add total round counter as derived attribute in Game

class Game(models.Model):
    GAME_STATES = (("W", "Waiting"),
                  ("R", "In Progress"),
                  ("J", "Judging"),
                  ("F", "Finished"))
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    points = models.IntegerField()
    game_state = models.CharField(max_length=1, choices=GAME_STATES, default='W')
    #number_of_rounds = models.Count("AppUser__id", filter=
    
    keeper_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    hosting_group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    users_playing = models.ManyToManyField(AppUser,through="Playing",related_name="users_playing")

class Task(models.Model):
    TASK_TYPES = (("L", "Go to location"),
                  ("R", "Pick up litter"))
                  #TBC
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE) 
    task_number = models.IntegerField() #Effective PK. This is a weak entity on Game
    
    task_type = models.CharField(max_length=1, choices=TASK_TYPES)
    points = models.IntegerField()

    completed_by = models.ManyToManyField(AppUser,through="Completion",related_name="completions")

    class Meta:
        unique_together = ("game_id", "task_number")

#Lobby equivalent. GameID may be used for the game code
class Playing(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE) 
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE) 
    active_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    final_position = models.IntegerField()

    class Meta:
        unique_together = ("user_id", "game_id")

#Task submission
class Completion(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    submission_uri = models.CharField(max_length=128)

    class Meta:
        unique_together = ("user_id", "task_id")
