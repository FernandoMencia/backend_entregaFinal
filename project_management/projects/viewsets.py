#permissions y authentication para que solo accedan ususarios autenticados
from .models import Project, Task
from rest_framework import viewsets, permissions, authentication 
from .serializers import ProjectSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'
    
    #para acceder a este viewset hay que estar autenticado
    Authentication_clases = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    
    #para acceder a este viewset hay que estar autenticado
    Authentication_clases = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]