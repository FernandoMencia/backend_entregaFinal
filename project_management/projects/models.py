from django.db import models
from django.contrib.auth.models import User


# Un proyecto puede tener muchas tareas, pero una tarea pertenece solo a un proyecto
# Relación uno a muchos

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
# Se relacionan las tarea con los proyectos a través de la fk por defecto (id)
# Se quiere que un posible borrado del proyecto, borre también las tareas (CASCADE)
class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
    #assigned_to = models.CharField(max_length=100) #se cambiará para relacionarlo con User
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


