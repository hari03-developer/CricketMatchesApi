from django.contrib import admin
from cricketapp.models import Team,Player,Match,Point

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display=['id','name','logoUri','clubstate']

class PlayerAdmin(admin.ModelAdmin):
    list_display=['id','firstName','lastName','imageUri','playerjerseynumber','country']

class MatchAdmin(admin.ModelAdmin):
    list_display=['id','match','winner']

class PointAdmin(admin.ModelAdmin):
    list_display=['id','team','points']


admin.site.register(Team,TeamAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Match,MatchAdmin)
admin.site.register(Point,PointAdmin)
