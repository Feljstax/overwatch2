from django.db import models

# Create your models here.
""" class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    tutorial_url = models.CharField(max_length=200, blank=False, default='')
    image_path = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False) """



class Hero(models.Model):
    name = models.CharField(max_length=128, blank=False)
    hp = models.IntegerField(blank=False)
    pick_ranking = models.IntegerField(blank=True, null=True)
    role_type = models.ForeignKey('Role', on_delete=models.CASCADE)
    #pass


class Ability(models.Model):
    ability_1 = models.CharField(max_length=500, blank=False)
    ability_2 = models.CharField(max_length=500, blank=False)
    ability_3 = models.CharField(max_length=500, blank=True, null=True)
    ability_4 = models.CharField(max_length=500, blank=True, null=True)
    hero_id = models.ForeignKey(Hero, on_delete=models.CASCADE)
    #pass

class Role(models.Model):
    role_type = models.CharField(max_length=280)
    #pass

class Team_composition(models.Model):
    comp_name = models.CharField(max_length=500)
    role_teamcomps = models.ManyToManyField(Role)

