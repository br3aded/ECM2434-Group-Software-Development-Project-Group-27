from django.db import models
from user.models import AppUser

# Create your models here.

class Group(models.Model):
    group_leader = models.ForeignKey(AppUser,on_delete=models.PROTECT)#change?
    max_players = models.IntegerField(default=8)

    group_members = models.ManyToManyField(AppUser, through="GroupMembers", related_name="group_members")

    @property
    def all_members(self):
        return [self.group_leader] + list(self.group_members.all())
    
class GroupMembers(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE) 
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE) 
    points_earned = models.IntegerField(default=0) #keeps a tally of points over the whole game

    class Meta:
        unique_together = ("user_id", "group_id")
