from django.contrib import admin

from .models import Game,Task,Player, Completion

admin.site.register(Game)
admin.site.register(Task)
admin.site.register(Player)
admin.site.register(Completion)