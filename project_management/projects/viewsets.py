from .models import Project, Task
from rest_framework import viewsets, permissions, authentication
from .serializers import ProjectSerializer, TaskSerializer
from .utils import send_notification, get_all_user_emails

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project = serializer.save()
        subject = f'New Project Created: {project.name}'
        message = f'A new project has been created:\n\nName: {project.name}\nDescription: {project.description}'
        recipients = get_all_user_emails()
        send_notification(subject, message, recipients)

    def perform_update(self, serializer):
        project = serializer.save()
        subject = f'Project Updated: {project.name}'
        message = f'The project has been updated:\n\nName: {project.name}\nDescription: {project.description}'
        recipients = get_all_user_emails()
        send_notification(subject, message, recipients)

    def perform_destroy(self, instance):
        subject = f'Project Deleted: {instance.name}'
        message = f'The project "{instance.name}" has been deleted.'
        recipients = get_all_user_emails()
        send_notification(subject, message, recipients)
        instance.delete()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save()
        subject = f'New Task Created: {task.name}'
        message = f'A new task has been created in project "{task.project.name}":\n\nName: {task.name}\nDescription: {task.description}'
        recipients = get_all_user_emails()
        send_notification(subject, message, recipients)

    def perform_update(self, serializer):
        task = serializer.save()
        subject = f'Task Updated: {task.name}'
        message = f'The task has been updated in project "{task.project.name}":\n\nName: {task.name}\nDescription: {task.description}'
        recipients = get_all_user_emails()
        send_notification(subject, message, recipients)

    def perform_destroy(self, instance):
        subject = f'Task Deleted: {instance.name}'
        message = f'The task "{instance.name}" in project "{instance.project.name}" has been deleted.'
        recipients = get_all_user_emails()
        send_notification(subject, message, recipients)
        instance.delete()
