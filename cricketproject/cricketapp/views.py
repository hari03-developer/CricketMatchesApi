from django.shortcuts import render
from django.views.generic import View
from cricketapp.models import Team,Player,Match,Point
# import json
from django.http import HttpResponse
# from  django.core.serializers import serialize
from cricketapp.mixins import SerializeMixin

### Team list
# Create your views here.
class TeamDetailsCBV(SerializeMixin,View):
    def get(self,request,id, *args,**kwargs):
        team= Team.objects.get(id=id)       
        json_data= self.serialize([team,])
        return HttpResponse(json_data,content_type='application/json')

class TeamListCBV(SerializeMixin,View):
    def get(self,request, *args,**kwargs):
        team_qs= Team.objects.all()
        json_data= self.serialize(team_qs)
        return HttpResponse(json_data,content_type='application/json')


### Player list and Details
# Create your views here.
class PlayerDetailsCBV(SerializeMixin,View):
    def get(self,request,id, *args,**kwargs):
        player= Player.objects.get(id=id)       
        json_data= self.serialize([player,])
        return HttpResponse(json_data,content_type='application/json')

class PlayerListCBV(SerializeMixin,View):
    def get(self,request, *args,**kwargs):
        player_qs= Player.objects.all()
        json_data= self.serialize(player_qs)
        return HttpResponse(json_data,content_type='application/json')

### Match list and Details
# Create your views here.
class MatchDetailsCBV(SerializeMixin,View):
    def get(self,request,id, *args,**kwargs):
        match= Match.objects.get(id=id)       
        json_data= self.serialize([match,])
        return HttpResponse(json_data,content_type='application/json')

class MatchListCBV(SerializeMixin,View):
    def get(self,request, *args,**kwargs):
        match_qs= Match.objects.all()
        json_data= self.serialize(match_qs)
        return HttpResponse(json_data,content_type='application/json')

### Points list and details
# Create your views here.
class PointsDetailsCBV(SerializeMixin,View):
    def get(self,request,id, *args,**kwargs):
        point= Point.objects.get(id=id)       
        json_data= self.serialize([point,])
        return HttpResponse(json_data,content_type='application/json')

class PointsListCBV(SerializeMixin,View):
    def get(self,request, *args,**kwargs):
        point_qs= Point.objects.all()
        json_data= self.serialize(point_qs)
        return HttpResponse(json_data,content_type='application/json')