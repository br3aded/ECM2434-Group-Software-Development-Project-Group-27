from django.contrib import admin

from .models import User,Item, Purchases

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Purchases)
