from django.contrib import admin

from .models import AppUser,Item

admin.site.register(AppUser)
admin.site.register(Item)
