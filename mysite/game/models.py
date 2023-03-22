from django.db import models
from user.models import AppUser
from home.models import Group
from django.db import models
from django.utils import timezone

ROUND_POINTS_PER_USER = 100

#Note for all ManyToMany relations, the django M2M field is stored in
#what would be the destination side of the arrow in the ER diagram

class Game(models.Model):
    GAME_STATES = ((0, "waitingForPlayers"),
                  (1, "settingTask"),
                  (2, "respondToTask"),
                  (3, "waitingForRanking"),
                  (4, "displayCurrentResults"),
                  (5, "endOfGame"))
    game_name = models.CharField(max_length=20,default="Game")
    game_code = models.CharField(max_length=5,null=True)
    start_datetime = models.DateTimeField(default=timezone.now)
    game_state = models.IntegerField(choices=GAME_STATES, default=0)
    max_rounds = models.IntegerField(default=5)

    current_round_number = models.IntegerField(default=0)
    current_round_name = models.CharField(max_length=64, default="Task")
    
    hosting_group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    
    submissions = models.ManyToManyField(AppUser,through="Submission",related_name="game_submissions")

    @property
    def points_per_round(self):
        return hosting_group.group_members.objects.count() * ROUND_POINTS_PER_USER
        #double check this works

    def __str__(self):
        return self.game_name

class Submission(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE) 
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE) 
    submission = models.BinaryField(null=True)
    
    class Meta:
        unique_together = ("user_id", "game_id")


