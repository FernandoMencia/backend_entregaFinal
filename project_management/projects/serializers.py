from rest_framework import serializers
from .models import Project, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        

# Se incluyen todas (many= True) las tareas asociadas a un proyecto (relación uno a muchos)
# este serializer no es para actualizar tareas (read_only = True)
class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
