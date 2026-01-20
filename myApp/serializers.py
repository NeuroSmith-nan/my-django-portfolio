from rest_framework import serializers
from .models import Experience
from .models import Skill
from .models import Project

class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id','image','title','tools','description','start_date','end_date']

class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','name','icon','level']

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','image','name','tools','description','github_link','demo_link','start_date','end_date']
