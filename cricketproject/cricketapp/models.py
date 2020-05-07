from django.db import models

# Create your models here.
class Team(models.Model):
    # identifier=models.IntegerField()
    name=models.CharField(max_length=64)
    logoUri=models.ImageField()
    clubstate=models.CharField(max_length=64)

class Player(models.Model):
    # identifier=models.IntegerField()
    firstName=models.CharField(max_length=64)
    lastName=models.CharField(max_length=64)
    imageUri=models.ImageField()
    playerjerseynumber=models.IntegerField()
    country=models.CharField(max_length=64)

class Match(models.Model):
    match=models.CharField(max_length=64)
    winner=models.CharField(max_length=64)

class Point(models.Model):
    team=models.CharField(max_length=64)
    points=models.IntegerField() 