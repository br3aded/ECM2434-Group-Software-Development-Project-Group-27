from django.contrib import admin

from .models import Game,Task,Completion


admin.site.register(Task)
#admin.site.register(Player)
admin.site.register(Completion)

'''
class GameAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.game_name
'''
        
admin.site.register(Game)