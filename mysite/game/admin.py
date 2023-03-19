from django.contrib import admin

from .models import Game,Task,Submission

admin.site.register(Task)
#admin.site.register(Player)
admin.site.register(Submission)

admin.site.register(Game)
