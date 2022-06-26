from rest_framework import serializers
#from tutorials.models import Tutorial
from heroes.models import Hero


# class TutorialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tutorial
#         fields = ('id', 'title', 'tutorial_url', 'image_path', 'description',
#                   'published')

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'hp', 'pick_ranking', 'role_type')

""" class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('role_type') """