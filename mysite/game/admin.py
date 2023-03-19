from django.contrib import admin

from .models import Game,Task

admin.site.register(Task)
#admin.site.register(Player)
#admin.site.register(Completion)

admin.site.register(Game)
