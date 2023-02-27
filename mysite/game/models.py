from django.db import models
from user.models import AppUser
from home.models import Group

#Note for all ManyToMany relations, the django M2M field is stored in
#what would be the destination side of the arrow in the ER diagram

#TODO:
#Add total round counter as derived attribute in Game

class Game(models.Model):
    GAME_STATES = ((0, "waitingForPlayers"),
                  (1, "settingTask"),
                  (2, "respondToTask"),
                  (3, "waitingForRanking"),
                  (4, "displayCurrentResults"),
                  (5, "endOfGame"))
    game_name = models.CharField(max_length=20,default= 0)
    game_code = models.CharField(max_length=5, default= 0)
    start_datetime = models.DateTimeField()
    #points = models.IntegerField()
    game_state = models.IntegerField(choices=GAME_STATES, default=0)
    #number_of_rounds = models.Count("AppUser__id", filter=
    
    keeper_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    hosting_group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    users_playing = models.ManyToManyField(AppUser,through="Playing",related_name="users_playing")

    def __str__(self):
        return self.game_name

class Task(models.Model):
    TASK_TYPES = (('T', "Default"),
                  ('L', "Location"))
                  #TBC, currently not in use
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE) 
    task_number = models.IntegerField() #Effective PK. This is a weak entity on Game

    task_name = models.CharField(max_length=128, default="Task")
    task_type = models.CharField(max_length=1, choices=TASK_TYPES)
    task_description = models.CharField(max_length=128, null=True)
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
