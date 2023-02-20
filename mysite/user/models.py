from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    hash_password = models.CharField(max_length=64)
    points = models.IntegerField()

#Included here since no other entity uses cosmetics
class Item(models.Model):
    ITEM_TYPES=(("A", "Badge"),
                ("B", "Background"),
                ("C", "CallingCard"))
    item_name = models.CharField(max_length=32)
    item_type = models.CharField(max_length=1,choices=ITEM_TYPES)
    points = models.IntegerField()

#Buys equivalent
class Purchases(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "item_id")

    
