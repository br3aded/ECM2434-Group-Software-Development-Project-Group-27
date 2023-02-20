from django.db import models
from user.models import User

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=32)
    group_leader = models.ForeignKey(User,on_delete=models.PROTECT)#change?

class GroupMembers(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ("group_id", "user_id")
