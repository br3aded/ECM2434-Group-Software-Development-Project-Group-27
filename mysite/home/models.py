from django.db import models
from user.models import AppUser

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=32)
    group_leader = models.ForeignKey(AppUser,on_delete=models.PROTECT)#change?

    group_members = models.ManyToManyField(AppUser, related_name="group_members")
