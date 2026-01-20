from django.shortcuts import render
from rest_framework import viewsets
# import Experiaence
from .models import Experience
from .serializers import ExperienceSerializers
# import Skill
from .models import Skill
from .serializers import SkillSerializers
# import Project
from .models import Project
from .serializers import ProjectSerializers

# Create your views here.
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers