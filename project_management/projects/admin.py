# Al registrar los modelos tengo acceso a ellos desde la interfaz admin
# Si no se hace esto no se puede acceder a los modelos desde la interfaz admin

from django.contrib import admin
from .models import Project, Task

# Se registran los modelos con personalización, se podrían incluir opciones de ordenamiento, edición, etc.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date', 'status')
    search_fields = ('id', 'name', 'status')
    list_filter = ('id', 'status')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project', 'start_date', 'end_date', 'status', 'assigned_to')
    search_fields = ('id', 'name', 'status')
    list_filter = ('id', 'status', 'project', 'assigned_to')

