from django.db import models
from django.contrib.auth.models import User

##class User(models.Model):
##    email = models.CharField(max_length=64)
##    username = models.CharField(max_length=64)
##    hash_password = models.CharField(max_length=64)
##    points = models.IntegerField()

#Weak Entity that links base user with app user data
class AppUser(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField()

#Included here since no other entity uses cosmetics
class Item(models.Model):
    ITEM_TYPES=(("A", "Badge"),
                ("B", "Background"),
                ("C", "CallingCard"))
    item_name = models.CharField(max_length=32)
    item_type = models.CharField(max_length=1,choices=ITEM_TYPES)
    points = models.IntegerField()

    purchased_by = models.ManyToManyField(User)    
