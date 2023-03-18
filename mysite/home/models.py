from django.db import models
from user.models import AppUser

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=32)
    group_leader = models.ForeignKey(AppUser,on_delete=models.PROTECT)#change?

    group_members = models.ManyToManyField(AppUser, through="GroupMembers", related_name="group_members")

class GroupMembers(models.Model):
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE) 
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE) 
    final_position = models.IntegerField(default=0)
    points_earned = models.IntegerField(default=0) #keeps a tally of points over the whole game

    class Meta:
        unique_together = ("user_id", "group_id")
