
from rest_framework.serializers import ModelSerializer

from .models import Project,Task



##############
# Serializer #
############## 

class ProjectSerializer(ModelSerializer):
  class Meta:
    model = Project
    fields = '__all__'

class TaskSerializer(ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'

